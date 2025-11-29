# normalize_folder.py
# Usage:
#   python normalize_folder.py <input_dir> <output_dir>

import os, io, sys, ast, builtins, keyword, tokenize, re
import ast

def _is_name(node, s):
    return isinstance(node, ast.Name) and node.id == s

def _is_main_str(node):
    return isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value.strip("_") == "main"

def _is_name_eq_main(compare: ast.Compare) -> bool:
    # 支持: __name__ == '__main__' / "__main__" == __name__
    if len(compare.ops) != 1 or not isinstance(compare.ops[0], ast.Eq):
        return False
    left, right = compare.left, compare.comparators[0]
    return (_is_name(left, "__name__") and _is_main_str(right)) or (_is_main_str(left) and _is_name(right, "__name__"))

def _contains_name_eq_main(expr: ast.expr) -> bool:
    # if __name__ == '__main__' [and ...]
    if isinstance(expr, ast.Compare):
        return _is_name_eq_main(expr)
    if isinstance(expr, ast.BoolOp):  # e.g., A and (__name__ == '__main__')
        return any(_contains_name_eq_main(v) for v in expr.values)
    if isinstance(expr, ast.UnaryOp) and isinstance(expr.op, ast.Not):
        return _contains_name_eq_main(expr.operand)
    return False

class MainBlockStripper(ast.NodeTransformer):
    """删除模块顶层的 `if __name__ == '__main__': ...` 代码块（整块去掉）"""
    def visit_Module(self, node: ast.Module):
        new_body = []
        for stmt in node.body:
            if isinstance(stmt, ast.If) and _contains_name_eq_main(stmt.test):
                # 跳过整个 main-guard 块
                continue
            new_body.append(stmt)
        node.body = new_body
        return self.generic_visit(node)
# ---------- 0) Py2 print fixer (prefer lib2to3; fallback regex) ----------
def fix_py2_prints(src: str) -> str:
    try:
        from lib2to3 import refactor  # type: ignore
        tool = refactor.RefactoringTool(['lib2to3.fixes.fix_print'], options={'print_function': True})
        try:
            return str(tool.refactor_string(src, name='-'))
        except Exception:
            pass
    except Exception:
        pass

    out_lines = []
    for line in src.splitlines(True):
        m = re.match(r'^(\s*)print(?!\s*\()', line)
        if not m:
            out_lines.append(line)
            continue
        indent = m.group(1)
        rest = line[m.end():]
        rest = re.sub(r'^\s*', '', rest)

        m_redir = re.match(r'^>>\s*([A-Za-z_]\w*)\s*,\s*(.*)$', rest)
        if m_redir:
            target, expr = m_redir.group(1), m_redir.group(2).rstrip()
            if expr.endswith(','):
                expr = expr[:-1].rstrip()
                out_lines.append(f"{indent}print({expr}, file={target}, end=' ')\n")
            else:
                out_lines.append(f"{indent}print({expr}, file={target})\n")
            continue

        rest_stripped = rest.rstrip()
        if rest_stripped.endswith(','):
            exprs = rest_stripped[:-1].rstrip()
            out_lines.append(f"{indent}print({exprs}, end=' ')\n")
        else:
            out_lines.append(f"{indent}print({rest_stripped})\n")
    return ''.join(out_lines)

# ---------- 1) strip comments ----------
def strip_comments(src: str) -> str:
    out, prev_end = [], (1, 0)
    tok_gen = tokenize.generate_tokens(io.StringIO(src).readline)
    for tok_type, tok_str, start, end, _ in tok_gen:
        if tok_type == tokenize.COMMENT:
            continue
        srow, scol = start
        erow, ecol = end
        if prev_end[0] < srow:
            out.append("\n" * (srow - prev_end[0]))
            out.append(" " * scol)
        else:
            out.append(" " * max(0, scol - prev_end[1]))
        if tok_type not in (tokenize.NL, tokenize.ENCODING, tokenize.ENDMARKER):
            out.append(tok_str)
        prev_end = (erow, ecol)
    return "".join(out)

# ---------- 2) strip docstrings ----------
class DocstringStripper(ast.NodeTransformer):
    @staticmethod
    def _strip_first_str_expr(body):
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
            return body[1:]
        return body
    def visit_Module(self, n):   n.body = self._strip_first_str_expr(self.generic_visit_list(n.body)); return n
    def visit_FunctionDef(self, n): self.generic_visit(n); n.body = self._strip_first_str_expr(n.body); return n
    def visit_AsyncFunctionDef(self, n): self.generic_visit(n); n.body = self._strip_first_str_expr(n.body); return n
    def visit_ClassDef(self, n): self.generic_visit(n); n.body = self._strip_first_str_expr(n.body); return n
    # helper
    def generic_visit_list(self, items):
        out = []
        for x in items:
            out.append(self.visit(x))
        return out

# ---------- 3) helpers ----------
_BUILTINS = set(dir(builtins))
_KEYWORDS = set(keyword.kwlist)
_DUNDER_WHITELIST = {"__init__", "__call__", "__iter__", "__next__", "__enter__", "__exit__"}

def _is_renamable_ident(name: str) -> bool:
    if not name: return False
    if name in _BUILTINS or name in _KEYWORDS or name in _DUNDER_WHITELIST: return False
    if name.startswith("__") and name.endswith("__"): return False
    return True

def _walk_targets(target, out_names):
    if isinstance(target, ast.Name) and isinstance(target.ctx, ast.Store):
        out_names.append(target.id)
    elif isinstance(target, (ast.Tuple, ast.List)):
        for elt in target.elts:
            _walk_targets(elt, out_names)

# ---------- 4) main renamer ----------
class Renamer(ast.NodeTransformer):
    """
    统一命名（定义与引用一致）：
      - 类 C1, C2, ...
      - 函数 f1, f2, ...
      - 形参 v1, v2, ...
      - 局部变量 v1, v2, ...（每个函数作用域独立计数/映射）
      - 类属性 a1, a2, ...（仅限该类定义的属性：self.*；以及从该类构造出的变量实例的属性）

    不更改外部库/未知对象属性名（如 .most_common 保留）。
    """
    def __init__(self):
        # 全局（模块级）定义映射：类与函数名 -> 规范名（用于引用处替换）
        self.global_defs = {}     # {old: new}
        self.func_count = 0
        self.class_count = 0

        # 作用域栈：每一层是一个 dict（形参+局部变量的映射）
        self.scope_stack = []

        # 类上下文栈：每个类一个 {attr_old: attr_new}
        self.class_attr_stack = []
        # 当前函数是否处于类方法中，以及该方法的“self”参数名（已规范化后的，一般是 v1）
        self.self_param_stack = []

        # 变量的“来源类”简单跟踪（仅记录由 ClassName(...) 构造的变量）
        self.var_instance_class_stack = []  # list[dict[varname] -> class_new_name]

    # ---- utilities ----
    def _enter_scope(self):
        self.scope_stack.append({})
        self.var_instance_class_stack.append({})
    def _exit_scope(self):
        self.scope_stack.pop()
        self.var_instance_class_stack.pop()

    def _map_local(self, name: str) -> str:
        cur = self.scope_stack[-1]
        if name not in cur:
            cur[name] = f"v{len(cur) + 1}"
        return cur[name]

    def _lookup_local(self, name: str):
        for m in reversed(self.scope_stack):
            if name in m:
                return m[name]
        return None

    def _record_instance(self, var_name: str, class_new: str):
        self.var_instance_class_stack[-1][var_name] = class_new

    def _lookup_instance_class(self, var_name: str):
        for m in reversed(self.var_instance_class_stack):
            if var_name in m:
                return m[var_name]
        return None

    def _new_func(self, old=None):
        self.func_count += 1
        new = f"f{self.func_count}"
        if old: self.global_defs[old] = new
        return new

    def _new_class(self, old=None):
        self.class_count += 1
        new = f"C{self.class_count}"
        if old: self.global_defs[old] = new
        return new

    def _map_class_attr(self, name: str) -> str:
        cur = self.class_attr_stack[-1]
        if name not in cur:
            cur[name] = f"a{len(cur) + 1}"
        return cur[name]

    # ---- Module ----
    def visit_Module(self, node: ast.Module):
        self._enter_scope()
        self.class_attr_stack = []
        self.self_param_stack = []
        self.generic_visit(node)
        self._exit_scope()
        return node

    # ---- Class ----
    def visit_ClassDef(self, node: ast.ClassDef):
        if _is_renamable_ident(node.name):
            node.name = self._new_class(node.name)
        # 新的类属性表
        self.class_attr_stack.append({})
        self._enter_scope()
        # 访问类体
        self.generic_visit(node)
        self._exit_scope()
        self.class_attr_stack.pop()
        return node

    # ---- Function / Method ----
    def visit_FunctionDef(self, node: ast.FunctionDef):
        if _is_renamable_ident(node.name):
            node.name = self._new_func(node.name)
        # 进入新函数作用域
        self._enter_scope()

        # 处理形参：统一为 v1,v2,... （并记录“self”名：类方法中第一个参数）
        self_name = None
        # 如果在类内，默认把第一个参数当作“self”
        in_class = len(self.class_attr_stack) > 0
        all_args = []
        for field in ["posonlyargs", "args", "kwonlyargs"]:
            all_args.extend(getattr(node.args, field, []))
        if in_class and all_args:
            self_name = all_args[0].arg

        def handle_arg(a: ast.arg):
            if _is_renamable_ident(a.arg):
                a.arg = self._map_local(a.arg)
            return a.arg

        first_param_new = None
        # 按顺序重命名
        for field in ["posonlyargs", "args", "kwonlyargs"]:
            lst = getattr(node.args, field, [])
            for i, a in enumerate(lst):
                newname = handle_arg(a)
                if i == 0 and self_name is not None:
                    first_param_new = newname
        if node.args.vararg and _is_renamable_ident(node.args.vararg.arg):
            node.args.vararg.arg = self._map_local(node.args.vararg.arg)
        if node.args.kwarg and _is_renamable_ident(node.args.kwarg.arg):
            node.args.kwarg.arg = self._map_local(node.args.kwarg.arg)

        # 进入/退出“self”上下文
        if in_class:
            self.self_param_stack.append(first_param_new or "v1")
        else:
            self.self_param_stack.append(None)

        self.generic_visit(node)

        self.self_param_stack.pop()
        self._exit_scope()
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        return self.visit_FunctionDef(node)  # 同步逻辑

    # ---- Name (locals & global defs) ----
    def visit_Name(self, node: ast.Name):
        # 1) 全局定义引用（类/函数名）
        if node.id in self.global_defs:
            node.id = self.global_defs[node.id]
            return node
        # 2) 局部映射（参数 + 局部）
        mapped = self._lookup_local(node.id)
        if mapped:
            node.id = mapped
        return node

    # ---- Local variable declarations (collect on Store) ----
    def visit_Assign(self, node: ast.Assign):
        # 记录局部变量（Store）
        names = []
        for t in node.targets:
            _walk_targets(t, names)
        for nm in names:
            if _is_renamable_ident(nm):
                new = self._map_local(nm)
                # 跟踪“由某类构造”的变量类型：var = C1(...)
        # 简单类型跟踪：var = ClassName(...)
        try:
            if isinstance(node.value, ast.Call):
                fn = node.value.func
                if isinstance(fn, ast.Name) and fn.id in self.global_defs.values():
                    class_new = fn.id
                    for t in node.targets:
                        if isinstance(t, ast.Name):
                            self._record_instance(t.id, class_new)
        except Exception:
            pass

        self.generic_visit(node)
        return node

    def visit_AnnAssign(self, node: ast.AnnAssign):
        # 处理目标名称
        tgt_names = []
        _walk_targets(node.target, tgt_names)
        for nm in tgt_names:
            if _is_renamable_ident(nm):
                self._map_local(nm)
        self.generic_visit(node)
        return node

    def visit_AugAssign(self, node: ast.AugAssign):
        tgt_names = []
        _walk_targets(node.target, tgt_names)
        for nm in tgt_names:
            if _is_renamable_ident(nm):
                self._map_local(nm)
        self.generic_visit(node)
        return node

    def visit_For(self, node: ast.For):
        tgt_names = []
        _walk_targets(node.target, tgt_names)
        for nm in tgt_names:
            if _is_renamable_ident(nm):
                self._map_local(nm)
        self.generic_visit(node)
        return node

    def visit_With(self, node: ast.With):
        for item in node.items:
            if item.optional_vars is not None:
                tgt_names = []
                _walk_targets(item.optional_vars, tgt_names)
                for nm in tgt_names:
                    if _is_renamable_ident(nm):
                        self._map_local(nm)
        self.generic_visit(node)
        return node

    # ---- Attribute: class field normalization ----
    def visit_Attribute(self, node: ast.Attribute):
        # 先递归
        self.generic_visit(node)

        # 仅改两类：
        #  (1) 在类方法里，base 是“self 参数”（已改名，一般是 v1）
        #  (2) base 变量被我们记录为“由某个已知类构造的实例”
        base = node.value
        if isinstance(base, ast.Name):
            # (1) 类方法里的 self.*
            if self.self_param_stack and self.self_param_stack[-1] and base.id == self.self_param_stack[-1]:
                if self.class_attr_stack:
                    node.attr = self._map_class_attr(node.attr)
                return node

            # (2) 类外部：若 base 来源于某个已知类的构造
            cls = self._lookup_instance_class(base.id)
            if cls is not None:
                # 使用“最近的类上下文”的属性表？这里做全局属性名映射不安全，
                # 我们采用“按类名统一”的映射表：为每个类名维护独立 attr_map
                # 简化：沿用当前最近的 class_attr_map（常见 LeetCode 单类场景）
                if self.class_attr_stack:
                    node.attr = self._map_class_attr(node.attr)
                return node

        return node

# ---------- 5) Orchestrator ----------
def normalize_python(src: str) -> str:
    # Py2 print -> Py3
    src = fix_py2_prints(src)
    # comments
    no_comments = strip_comments(src)
    # parse
    try:
        tree = ast.parse(no_comments)
    except SyntaxError:
        tree = ast.parse(src)
    # docstrings
    tree = DocstringStripper().visit(tree)
    tree = MainBlockStripper().visit(tree)
    # rename
    ren = Renamer()
    tree = ren.visit(tree)
    ast.fix_missing_locations(tree)
    # unparse & trim
    code = ast.unparse(tree)
    code = "\n".join(line.rstrip() for line in code.splitlines()).strip() + "\n"
    return code

# ---------- 6) Folder processing ----------
def process_folder(in_dir: str, out_dir: str):
    in_dir = os.path.abspath(in_dir)
    out_dir = os.path.abspath(out_dir)
    for root, _dirs, files in os.walk(in_dir):
        for fname in files:
            if not fname.endswith(".py"):
                continue
            src_path = os.path.join(root, fname)
            rel = os.path.relpath(src_path, in_dir)
            dst_path = os.path.join(out_dir, rel)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
                src = f.read()
            try:
                norm = normalize_python(src)
                status = "OK"
            except Exception as e:
                norm = src
                status = f"WARN ({e})"
            with open(dst_path, "w", encoding="utf-8", errors="ignore") as f:
                f.write(norm)
            print(f"[{status}] {rel}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python normalize_folder.py <input_dir> <output_dir>")
        sys.exit(1)
    process_folder(sys.argv[1], sys.argv[2])

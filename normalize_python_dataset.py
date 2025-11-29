#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
normalize_python_dataset.py

对 dataset_root/{llm_code,human_code} 下的所有 .py 文件做 AST 级归一化（alpha-renaming）：
- 统一本地变量名/参数名/for/with/except 临时变量为 v1.. / a1..
- 统一模块内自定义函数名为 f1..（同时更新模块内调用）
- 统一类名为 C1..（同时更新模块内该类被直接引用的地方）
- 保留 import 的名字、内置名、self/cls、属性名（obj.attr 不改）、魔术名(__init__等)
- 输出到 normalized/{llm_code,human_code}，并生成 manifest_normalized.csv

用法:
  python normalize_python_dataset.py --in-root dataset_root --out-root normalized
  # 就地覆盖（谨慎使用）
  # python normalize_python_dataset.py --in-root dataset_root --out-root dataset_root --inplace
"""

import argparse
import csv
import hashlib
import sys
from pathlib import Path
import shutil
import ast
import builtins
from typing import Dict, List, Optional, Set, Tuple

# -------------------- 工具 --------------------

def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8", errors="replace")).hexdigest()

def read_text(p: Path) -> Optional[str]:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        try:
            return p.read_text(encoding="latin-1", errors="replace")
        except Exception:
            return None

def write_text(p: Path, data: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(data, encoding="utf-8", errors="replace")

def is_magic_name(name: str) -> bool:
    return len(name) >= 4 and name.startswith("__") and name.endswith("__")

# -------------------- 作用域与映射 --------------------

BUILTIN_NAMES: Set[str] = set(dir(builtins))
RESERVED_HARD = {"self", "cls"}

class Scope:
    """
    每个作用域维护：变量映射、计数器。
    - var_map: 普通变量/临时名 -> v1, v2, ...
    - arg_map: 形参名 -> a1, a2, ...
    - func_map: 本作用域“可见的函数名”（在外层作用域登记） -> f1, f2, ...
    - class_map: 同上（类名） -> C1, C2, ...
    - preserved: 不可改名的符号（import/builtin/魔术名/保留名）
    """
    def __init__(self, parent: Optional["Scope"]=None):
        self.parent = parent
        self.var_map: Dict[str, str] = {}
        self.arg_map: Dict[str, str] = {}
        self.func_map: Dict[str, str] = {}   # 名称分配在“定义所在的上层作用域”
        self.class_map: Dict[str, str] = {}
        self.preserved: Set[str] = set()

        # 计数器
        self._var_i = 1
        self._arg_i = 1

    def new_var(self, original: str) -> str:
        if original in self.var_map:
            return self.var_map[original]
        name = f"v{self._var_i}"
        self._var_i += 1
        self.var_map[original] = name
        return name

    def new_arg(self, original: str) -> str:
        if original in self.arg_map:
            return self.arg_map[original]
        name = f"a{self._arg_i}"
        self._arg_i += 1
        self.arg_map[original] = name
        return name

    # 作用域链查询
    def lookup_any(self, name: str) -> Optional[str]:
        # 优先各类映射
        if name in self.arg_map: return self.arg_map[name]
        if name in self.var_map: return self.var_map[name]
        if name in self.func_map: return self.func_map[name]
        if name in self.class_map: return self.class_map[name]
        if self.parent:
            return self.parent.lookup_any(name)
        return None

    def is_preserved(self, name: str) -> bool:
        if name in self.preserved: return True
        if self.parent: return self.parent.is_preserved(name)
        return False

    def set_preserved(self, names: List[str]):
        for n in names:
            if n: self.preserved.add(n)

# -------------------- 预收集（import/定义名） --------------------

class PreCollector(ast.NodeVisitor):
    """
    先做一遍遍历，收集：
    - import / from import 得到的名字（preserved）
    - 记录所有函数定义、类定义的“原名”出现顺序（在上层作用域登记）
    - 全局赋值的“名字”（也算变量，统一）
    """
    def __init__(self):
        self.module_scope = Scope(None)
        self.current_scope = self.module_scope
        self.func_counter = 1
        self.class_counter = 1

    def push_scope(self):
        self.current_scope = Scope(self.current_scope)

    def pop_scope(self):
        assert self.current_scope.parent is not None
        self.current_scope = self.current_scope.parent

    def visit_Import(self, node: ast.Import):
        # import numpy as np  -> preserve 'np'
        # import os           -> preserve 'os'
        keep = []
        for alias in node.names:
            keep.append(alias.asname if alias.asname else alias.name.split(".")[0])
        self.current_scope.set_preserved(keep)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        keep = []
        for alias in node.names:
            if alias.name == "*":
                # 无法确定，保守：不做任何本地改名限制（这里仅记一个标记）
                # 实际变换器仍只会改本地变量，不会动属性/未知符号
                continue
            keep.append(alias.asname if alias.asname else alias.name)
        self.current_scope.set_preserved(keep)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # 函数名在“外层作用域”登记（模块或类作用域）
        if not is_magic_name(node.name):
            self.current_scope.func_map.setdefault(node.name, f"f{self.func_counter}")
            self.func_counter += 1
        # 进入函数体作用域
        self.push_scope()
        # 形参名字预分配
        for arg in node.args.posonlyargs + node.args.args:
            if arg.arg not in RESERVED_HARD and not is_magic_name(arg.arg):
                self.current_scope.new_arg(arg.arg)
        if node.args.vararg and node.args.vararg.arg not in RESERVED_HARD:
            self.current_scope.new_arg(node.args.vararg.arg)
        for arg in node.args.kwonlyargs:
            if arg.arg not in RESERVED_HARD:
                self.current_scope.new_arg(arg.arg)
        if node.args.kwarg and node.args.kwarg.arg not in RESERVED_HARD:
            self.current_scope.new_arg(node.args.kwarg.arg)

        self.generic_visit(node)
        self.pop_scope()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.visit_FunctionDef(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        if not is_magic_name(node.name):
            self.current_scope.class_map.setdefault(node.name, f"C{self.class_counter}")
            self.class_counter += 1
        # 类体是新的作用域
        self.push_scope()
        self.generic_visit(node)
        self.pop_scope()

# -------------------- 归一化变换器 --------------------

class Normalizer(ast.NodeTransformer):
    def __init__(self, pre: PreCollector):
        self.pre = pre
        self.current_scope = pre.module_scope

    # ----- 作用域管理 -----
    def push(self):
        self.current_scope = Scope(self.current_scope)

    def pop(self):
        assert self.current_scope.parent is not None
        self.current_scope = self.current_scope.parent

    # ----- 名称判定 -----
    def _eligible_var(self, name: str) -> bool:
        if not name: return False
        if name in RESERVED_HARD: return False
        if is_magic_name(name): return False
        if name in BUILTIN_NAMES and not self.current_scope.lookup_any(name):
            # 如果是内置并且没被局部遮蔽，就不要改
            return False
        if self.current_scope.is_preserved(name):
            return False
        return True

    # ----- 变量 & 名称引用 -----
    def visit_Name(self, node: ast.Name):
        # 属性名（obj.attr）走 Attribute，不会到这里；这里只管裸 Name
        mapped = self.current_scope.lookup_any(node.id)
        if isinstance(node.ctx, ast.Store):
            # 遇到新的赋值目标，按需分配
            if not mapped and self._eligible_var(node.id):
                mapped = self.current_scope.new_var(node.id)
        if mapped:
            return ast.copy_location(ast.Name(id=mapped, ctx=node.ctx), node)
        else:
            return node

    def _handle_target(self, target):
        # 在 Store 环境（赋值/for/with/except），提前为名字分配占位
        if isinstance(target, ast.Name):
            if self._eligible_var(target.id):
                self.current_scope.new_var(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                self._handle_target(elt)
        elif isinstance(target, ast.Starred):
            self._handle_target(target.value)
        # Attribute/Subscript 不动

    # ----- 赋值/for/with/except -----
    def visit_Assign(self, node: ast.Assign):
        for t in node.targets:
            self._handle_target(t)
        self.generic_visit(node)
        return node

    def visit_AnnAssign(self, node: ast.AnnAssign):
        self._handle_target(node.target)
        self.generic_visit(node)
        return node

    def visit_AugAssign(self, node: ast.AugAssign):
        self._handle_target(node.target)
        self.generic_visit(node)
        return node

    def visit_For(self, node: ast.For):
        self._handle_target(node.target)
        self.generic_visit(node)
        return node

    def visit_AsyncFor(self, node: ast.AsyncFor):
        return self.visit_For(node)

    def visit_With(self, node: ast.With):
        for item in node.items:
            if item.optional_vars:
                self._handle_target(item.optional_vars)
        self.generic_visit(node)
        return node

    def visit_AsyncWith(self, node: ast.AsyncWith):
        return self.visit_With(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler):
        if node.name and self._eligible_var(node.name):
            # except Exception as e:
            node.name = self.current_scope.new_var(node.name)
        self.generic_visit(node)
        return node

    # ----- 函数/类定义 -----
    def visit_FunctionDef(self, node: ast.FunctionDef):
        # 重命名函数名（在外层作用域登记过）
        if not is_magic_name(node.name):
            mapped = self.current_scope.lookup_any(node.name)
            if mapped:
                node.name = mapped

        # 新函数作用域
        self.push()
        # 形参替换为 a1,a2..
        def _rename_arg(arg: ast.arg):
            if arg.arg in RESERVED_HARD or is_magic_name(arg.arg):
                return
            new = self.current_scope.new_arg(arg.arg)
            arg.arg = new

        for a in node.args.posonlyargs + node.args.args:
            _rename_arg(a)
        if node.args.vararg: _rename_arg(node.args.vararg)
        for a in node.args.kwonlyargs:
            _rename_arg(a)
        if node.args.kwarg: _rename_arg(node.args.kwarg)

        self.generic_visit(node)
        self.pop()
        return node

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        return self.visit_FunctionDef(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        if not is_magic_name(node.name):
            mapped = self.current_scope.lookup_any(node.name)
            if mapped:
                node.name = mapped
        self.push()
        self.generic_visit(node)
        self.pop()
        return node

# -------------------- 单文件处理 --------------------

def normalize_code(source: str) -> Tuple[str, Dict[str, str]]:
    """
    返回 (normalized_source, info)
    解析失败时抛出异常
    """
    tree = ast.parse(source)
    # 先预收集
    pre = PreCollector()
    pre.visit(tree)

    # 归一化
    norm = Normalizer(pre)
    new_tree = norm.visit(tree)
    ast.fix_missing_locations(new_tree)

    # 反编译
    try:
        new_src = ast.unparse(new_tree)
    except Exception as e:
        # 极少数环境不支持 unparse；可以改用 astor（但本脚本保持纯标准库）
        raise e

    # 统一换行，末尾换行
    new_src = new_src.replace("\r\n", "\n").replace("\r", "\n")
    if not new_src.endswith("\n"):
        new_src += "\n"

    info = {
        "orig_sha256": sha256_hex(source),
        "norm_sha256": sha256_hex(new_src),
    }
    return new_src, info

# -------------------- 主流程 --------------------

def process_tree(in_root: Path, out_root: Path, inplace: bool=False) -> List[Dict]:
    """
    遍历 in_root/{llm_code,human_code}，把 .py 归一化写到 out_root 对应目录。
    返回 manifest 记录列表。
    """
    subsets = ["llm_code", "human_code"]
    manifest: List[Dict] = []
    for sub in subsets:
        in_dir = in_root / sub
        out_dir = (in_root if inplace else out_root) / sub
        out_dir.mkdir(parents=True, exist_ok=True)
        if not in_dir.exists():
            continue

        for p in in_dir.rglob("*.py"):
            rel = p.relative_to(in_root)
            dst = out_dir / p.name
            raw = read_text(p)
            if raw is None:
                # 读取失败，直接复制原文件
                try:
                    shutil.copy2(p, dst)
                except Exception:
                    pass
                manifest.append({
                    "subset": sub,
                    "orig_path": str(rel),
                    "norm_path": str(dst.relative_to(out_root if not inplace else in_root)),
                    "ok": 0,
                    "reason": "read_fail",
                    "orig_sha256": "",
                    "norm_sha256": "",
                })
                continue

            try:
                new_src, info = normalize_code(raw)
                write_text(dst, new_src)
                manifest.append({
                    "subset": sub,
                    "orig_path": str(rel),
                    "norm_path": str(dst.relative_to(out_root if not inplace else in_root)),
                    "ok": 1,
                    "reason": "",
                    **info,
                })
            except Exception as e:
                # 解析失败：保守地复制原文
                try:
                    shutil.copy2(p, dst)
                except Exception:
                    write_text(dst, raw)
                manifest.append({
                    "subset": sub,
                    "orig_path": str(rel),
                    "norm_path": str(dst.relative_to(out_root if not inplace else in_root)),
                    "ok": 0,
                    "reason": f"parse_or_unparse_fail: {type(e).__name__}",
                    "orig_sha256": sha256_hex(raw),
                    "norm_sha256": sha256_hex(raw),
                })
    return manifest

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in-root", default="dataset_root", help="输入数据根目录（包含 llm_code / human_code）")
    ap.add_argument("--out-root", default="normalized", help="归一化输出目录")
    ap.add_argument("--inplace", action="store_true", help="就地覆盖（谨慎）")
    ap.add_argument("--manifest-name", default="manifest_normalized.csv")
    args = ap.parse_args()

    in_root = Path(args.in_root).resolve()
    out_root = Path(args.out_root).resolve()

    if args.inplace:
        print(f"[WARN] In-place normalization: {in_root}")
        out_root = in_root
    else:
        out_root.mkdir(parents=True, exist_ok=True)

    rows = process_tree(in_root, out_root, inplace=args.inplace)

    # 写 manifest
    if rows:
        mf_path = (out_root if not args.inplace else in_root) / args.manifest_name
        with mf_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"[OK] Manifest written: {mf_path} ({len(rows)} files)")
    else:
        print("[WARN] No files processed.")

if __name__ == "__main__":
    main()

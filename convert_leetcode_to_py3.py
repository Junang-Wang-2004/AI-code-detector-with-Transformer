import os
import io
import shutil
from lib2to3 import refactor
import re

# =========================================================
# 配置区
# =========================================================

# 原始 Python2/混合风格代码目录（你的仓库路径）
SRC_DIR = r"D:\learning\APS360\project\leetcode_github\LeetCode-Solutions\Python"

# 输出 Python3 代码的新目录
DST_DIR = r"D:\learning\APS360\project\leetcode_github\LeetCode-Solutions\Python_py3"

# 是否删除 LeetCode 源代码的类型注释（例如 :type / :rtype）
REMOVE_LEETCODE_TYPE_COMMENTS = True

# =========================================================

# 获取 2to3 fixers
FIXERS = refactor.get_fixers_from_package("lib2to3.fixes")
REF = refactor.RefactoringTool(FIXERS)

# 匹配 LeetCode 旧式类型注释
LEETCODE_TYPE_LINE = re.compile(r"^\s*:(type|rtype)\b.*$", re.IGNORECASE)


def clean_leetcode_type_comments(code: str) -> str:
    """删除 LeetCode 风格的 :type / :rtype 注释"""
    if not REMOVE_LEETCODE_TYPE_COMMENTS:
        return code

    new_lines = []
    for line in code.splitlines():
        if LEETCODE_TYPE_LINE.match(line):
            continue
        new_lines.append(line)

    return "\n".join(new_lines) + "\n"


def convert_file(src_path: str, dst_path: str):
    """将单个 py 文件转换为 Python3 并写入 dst_path"""
    print(f"Converting: {src_path}")

    with io.open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        src_code = f.read()

    # 运行 2to3
    try:
        tree = REF.refactor_string(src_code, src_path)
        py3_code = str(tree)
    except Exception as e:
        print(f"  [WARN] 2to3 failed: {e}")
        py3_code = src_code  # 最后退回，不 crash

    # 清理 LeetCode 类型注释
    py3_code = clean_leetcode_type_comments(py3_code)

    # 创建必要的目录
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    # 写入到新路径
    with io.open(dst_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(py3_code)

    print(f"  Saved → {dst_path}")


def walk_and_convert(src_dir: str, dst_dir: str):
    """遍历整个 src_dir，将所有 .py 转换到 dst_dir"""
    for dirpath, dirnames, filenames in os.walk(src_dir):
        relative_dir = os.path.relpath(dirpath, src_dir)
        out_dir = os.path.join(dst_dir, relative_dir)

        for filename in filenames:
            if filename.endswith(".py"):
                src_file = os.path.join(dirpath, filename)
                dst_file = os.path.join(out_dir, filename)

                convert_file(src_file, dst_file)


if __name__ == "__main__":
    print(f"Source: {SRC_DIR}")
    print(f"Destination: {DST_DIR}")

    os.makedirs(DST_DIR, exist_ok=True)

    walk_and_convert(SRC_DIR, DST_DIR)

    print("\nAll done! Converted Python3 files saved in:")
    print(DST_DIR)

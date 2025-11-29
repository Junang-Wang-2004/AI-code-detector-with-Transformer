import os
import io
import shutil
import re

# ===================== 配置区 =====================

# 原始（已经转成 Python3 的）LeetCode 代码目录
SRC_ROOT = r"D:\learning\APS360\project\leetcode_github\Python_py3"

# 拆分后的输出目录（会自动创建，不会修改原始目录）
DST_ROOT = r"D:\learning\APS360\project\leetcode_github\Python_split"

# =================================================


def read_lines(path):
    with io.open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.readlines()


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def split_by_time_blocks(lines):
    """
    按 '# Time:' 这样的注释块拆分。
    返回 [chunk1_str, chunk2_str, ...] 或 None（表示不适合按这个方式拆）。
    """
    indices = []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("# Time"):
            indices.append(i)

    if len(indices) <= 1:
        return None  # 只有一个 Time 或没有 Time，不按这个拆

    header = lines[:indices[0]]  # 可能有 shebang / encoding / 通用 import

    chunks = []
    for k, start in enumerate(indices):
        end = indices[k + 1] if k + 1 < len(indices) else len(lines)
        chunk_lines = header + lines[start:end]
        chunks.append("".join(chunk_lines))
    return chunks


def split_by_solution_classes(lines):
    """
    如果没有多个 '# Time:'，退而求其次按 class Solution / Solution2 拆。
    """
    indices = []
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        # 匹配 class Solution( ... 或 class Solution2( ...
        if stripped.startswith("class Solution"):
            indices.append(i)

    if len(indices) <= 1:
        return None

    header = lines[:indices[0]]
    chunks = []
    for k, start in enumerate(indices):
        end = indices[k + 1] if k + 1 < len(indices) else len(lines)
        chunk_lines = header + lines[start:end]
        chunks.append("".join(chunk_lines))
    return chunks


def process_file(src_path, rel_path):
    """
    对单个 .py 文件做拆分或复制。
    """
    lines = read_lines(src_path)

    # 优先按 '# Time:' 拆
    chunks = split_by_time_blocks(lines)

    # 如果不行，再按 class Solution 拆
    if chunks is None:
        chunks = split_by_solution_classes(lines)

    dst_dir = os.path.join(DST_ROOT, os.path.dirname(rel_path))
    os.makedirs(dst_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(rel_path))[0]

    if not chunks:
        # 只有一个解法 → 原样复制
        dst_path = os.path.join(DST_ROOT, rel_path)
        shutil.copy2(src_path, dst_path)
        print(f"[COPY] {rel_path}")
        return

    # 有多个块 → 逐个写成新文件
    for idx, chunk in enumerate(chunks, start=1):
        new_name = f"{base_name}__part{idx}.py"
        dst_path = os.path.join(dst_dir, new_name)
        write_text(dst_path, chunk)
        print(f"[SPLIT] {rel_path} → {new_name}")


def walk_and_split():
    for dirpath, dirnames, filenames in os.walk(SRC_ROOT):
        rel_dir = os.path.relpath(dirpath, SRC_ROOT)
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            src_path = os.path.join(dirpath, fname)
            rel_path = os.path.join(rel_dir, fname) if rel_dir != "." else fname
            process_file(src_path, rel_path)


if __name__ == "__main__":
    print("SRC_ROOT:", SRC_ROOT)
    print("DST_ROOT:", DST_ROOT)
    os.makedirs(DST_ROOT, exist_ok=True)
    walk_and_split()
    print("Done.")

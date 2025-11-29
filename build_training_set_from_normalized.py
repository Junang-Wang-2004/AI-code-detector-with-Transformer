#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
把 leetcode_normalized 和 AIGCodeSet_normalized 合并成一个训练集：

- 两个目录结构类似：
    root/
        human_code/
        llm_code/
        manifest_normalized.csv

- 只保留 ok == 1 的样本
- 只保留代码非空行数 >= --min-lines 的样本
- 复制到 out_root/{human_code,llm_code}
- 生成合并后的 manifest_clean.csv
- 可选生成 all.jsonl（text/label/source）

用法示例：

python build_combined_training_set.py ^
  --leetcode-root "D:\learning\APS360\project\leetcode_github\leetcode_normalized" ^
  --aig-root      "D:\learning\APS360\project\leetcode_github\AIGCodeSet_normalized" ^
  --out-root      "D:\learning\APS360\project\leetcode_github\combined_train" ^
  --min-lines 20 ^
  --jsonl
"""

import argparse
import csv
import json
import shutil
from pathlib import Path


def count_nonempty_lines(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return 0
    return sum(1 for ln in text.splitlines() if ln.strip())


def process_root(root: Path,
                 source_name: str,
                 out_llm: Path,
                 out_human: Path,
                 min_lines: int,
                 make_jsonl: bool,
                 rows_out: list,
                 jsonl_records: list,
                 all_keys: set):
    """
    读取一个 normalized root (leetcode 或 AIGCodeSet)，
    把 ok==1 且行数>=min_lines 的样本复制到 out_root 里。
    """
    manifest_path = root / "manifest_normalized.csv"
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest not found: {manifest_path}")

    with manifest_path.open("r", encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            # 标记来源
            r["source"] = source_name

            # 只保留归一化成功的
            if str(r.get("ok", "0")).strip() != "1":
                r["copy_ok"] = "0"
                r["copy_reason"] = "ok!=1"
                rows_out.append(r)
                all_keys.update(r.keys())
                continue

            norm_rel = r.get("norm_path", "")
            if not norm_rel:
                r["copy_ok"] = "0"
                r["copy_reason"] = "no_norm_path"
                rows_out.append(r)
                all_keys.update(r.keys())
                continue

            src = (root / norm_rel).resolve()
            if not src.exists():
                r["copy_ok"] = "0"
                r["copy_reason"] = "src_missing"
                rows_out.append(r)
                all_keys.update(r.keys())
                continue

            # 行数过滤
            n_lines = count_nonempty_lines(src)
            r["lines"] = str(n_lines)
            if n_lines < min_lines:
                r["copy_ok"] = "0"
                r["copy_reason"] = f"too_short(<{min_lines})"
                rows_out.append(r)
                all_keys.update(r.keys())
                continue

            # 根据路径判断标签
            lower = norm_rel.replace("\\", "/").lower()
            fname = Path(norm_rel).name
            # 为避免两个数据集重名，统一加前缀
            prefixed_name = f"{source_name}__{fname}"

            if "/llm_code/" in lower or lower.startswith("llm_code/"):
                dst = out_llm / prefixed_name
                label = 1
            elif "/human_code/" in lower or lower.startswith("human_code/"):
                dst = out_human / prefixed_name
                label = 0
            else:
                # 不认识的子目录，当做人类
                dst = out_human / prefixed_name
                label = 0

            try:
                shutil.copy2(src, dst)
                r["copy_ok"] = "1"
                r["copy_reason"] = ""
            except Exception as e:
                r["copy_ok"] = "0"
                r["copy_reason"] = f"copy_fail:{type(e).__name__}"

            rows_out.append(r)
            all_keys.update(r.keys())

            # 可选导出 jsonl
            if make_jsonl and r["copy_ok"] == "1":
                try:
                    text = dst.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    text = ""
                rec_id = (
                    r.get("norm_path")
                    or r.get("orig_path")
                    or f"{source_name}:{dst.name}"
                )
                jsonl_records.append(
                    {
                        "id": rec_id,
                        "text": text,
                        "label": label,
                        "source": source_name,
                        "problem_id": r.get("problem_id", ""),
                    }
                )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leetcode-root", required=True,
                    help="leetcode_normalized 根目录")
    ap.add_argument("--aig-root", required=True,
                    help="AIGCodeSet_normalized 根目录")
    ap.add_argument("--out-root", required=True,
                    help="输出训练目录")
    ap.add_argument("--min-lines", type=int, default=20,
                    help="代码非空行数至少多少才保留 (default: 20)")
    ap.add_argument("--jsonl", action="store_true",
                    help="同时导出 all.jsonl（含 text/label/source）")
    args = ap.parse_args()

    leet_root = Path(args.leetcode_root).resolve()
    aig_root = Path(args.aig_root).resolve()
    out_root = Path(args.out_root).resolve()

    out_llm = out_root / "llm_code"
    out_human = out_root / "human_code"
    out_llm.mkdir(parents=True, exist_ok=True)
    out_human.mkdir(parents=True, exist_ok=True)

    rows_out = []
    jsonl_records = []
    all_keys = set()

    # 先处理 leetcode
    process_root(
        leet_root,
        "leetcode",
        out_llm,
        out_human,
        args.min_lines,
        args.jsonl,
        rows_out,
        jsonl_records,
        all_keys,
    )

    # 再处理 AIGCodeSet
    process_root(
        aig_root,
        "aigcodeset",
        out_llm,
        out_human,
        args.min_lines,
        args.jsonl,
        rows_out,
        jsonl_records,
        all_keys,
    )

    # 写出合并后的 manifest_clean.csv
    if rows_out:
        out_manifest = out_root / "manifest_clean.csv"
        fieldnames = sorted(all_keys)
        with out_manifest.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for r in rows_out:
                # 确保所有列都有值
                row_full = {k: r.get(k, "") for k in fieldnames}
                w.writerow(row_full)

    # 写出 all.jsonl
    if args.jsonl and jsonl_records:
        jsonl_path = out_root / "all.jsonl"
        with jsonl_path.open("w", encoding="utf-8") as f:
            for rec in jsonl_records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 简单汇总
    total = len(rows_out)
    ok = sum(1 for r in rows_out if r.get("copy_ok") == "1")
    print(f"[OK] copied: {ok}/{total} samples -> {out_root}")
    print(f"[OK] manifest: {out_root/'manifest_clean.csv'}")
    if args.jsonl:
        print(f"[OK] jsonl: {out_root/'all.jsonl'} ({len(jsonl_records)} records)")


if __name__ == "__main__":
    main()
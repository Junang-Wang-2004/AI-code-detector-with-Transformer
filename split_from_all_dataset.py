#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
从 combined_train/all.jsonl 里按 label 做 stratified 划分：
    -> train.jsonl / val.jsonl / test.jsonl

并且在写出时把 'text' 字段复制到 'code' 字段，
以兼容现有的 CodeBERT notebook（里面用 row['code']）。

用法示例：

python make_splits_from_all.py ^
  --all-jsonl "D:\learning\APS360\project\leetcode_github\combined_train\all.jsonl" ^
  --out-dir   "D:\learning\APS360\project\leetcode_github\combined_train\splits" ^
  --val-ratio 0.10 ^
  --test-ratio 0.10 ^
  --seed 42
"""

import argparse
import json
from pathlib import Path

from sklearn.model_selection import train_test_split


def read_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            rows.append(json.loads(ln))
    return rows


def write_jsonl(path: Path, rows):
    with path.open("w", encoding="utf-8") as f:
        for r in rows:
            # 复制一份 text -> code，兼容旧代码
            if "code" not in r:
                r["code"] = r.get("text", "")
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all-jsonl", required=True,
                    help="combined_train/all.jsonl's address")
    ap.add_argument("--out-dir", required=True,
                    help="output train/val/test.jsonl's address")
    ap.add_argument("--val-ratio", type=float, default=0.10,
                    help="val's ratio (default: 0.10)")
    ap.add_argument("--test-ratio", type=float, default=0.10,
                    help="test's ratio (default: 0.10)")
    ap.add_argument("--seed", type=int, default=42,
                    help="random seed")
    args = ap.parse_args()

    all_path = Path(args.all_jsonl).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = read_jsonl(all_path)
    print(f"[OK] loaded {len(rows)} samples from {all_path}")

    labels = []
    for r in rows:
        try:
            labels.append(int(r.get("label", 0)))
        except Exception:
            labels.append(0)

    # 先拆出 test
    train_val_rows, test_rows, train_val_y, test_y = train_test_split(
        rows, labels,
        test_size=args.test_ratio,
        random_state=args.seed,
        stratify=labels
    )

    # 再从 train_val 里拆 val
    # 注意：val 是 train_val 的一部分，所以这里的比例要按剩下的再算
    val_ratio_rel = args.val_ratio / (1.0 - args.test_ratio)

    train_rows, val_rows, train_y, val_y = train_test_split(
        train_val_rows, train_val_y,
        test_size=val_ratio_rel,
        random_state=args.seed,
        stratify=train_val_y
    )

    print(f"[SPLIT] train={len(train_rows)}  val={len(val_rows)}  test={len(test_rows)}")

    train_path = out_dir / "train.jsonl"
    val_path   = out_dir / "val.jsonl"
    test_path  = out_dir / "test.jsonl"

    write_jsonl(train_path, train_rows)
    write_jsonl(val_path,   val_rows)
    write_jsonl(test_path,  test_rows)

    print(f"[OK] wrote {train_path}")
    print(f"[OK] wrote {val_path}")
    print(f"[OK] wrote {test_path}")


if __name__ == "__main__":
    main()
import os
import io
import json
import time
import textwrap
import difflib
import requests

# ===================== 配置区 =====================

# 1. 人类代码目录（Python3 版本）
HUMAN_ROOT = r"D:\learning\APS360\project\leetcode_github\Python_py3"

# 2. AI 代码输出目录（会自动创建，不覆盖原文件）
AI_ROOT = r"D:\learning\APS360\project\leetcode_github\Python_ai_grok"

# 3. metadata 文件路径（JSONL，每行一条记录）
METADATA_PATH = r"D:\learning\APS360\project\leetcode_github\LeetCode-Solutions\python_ai_grok_metadata.jsonl"

# 4. OpenRouter 设置（API Key 请用环境变量 OPENROUTER_API_KEY）
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# 5. 使用的模型：Grok 4.1 Fast
MODEL = "x-ai/grok-4.1-fast"

# 6. 其他生成参数
VARIANTS_PER_FILE = 1    # 每个 human 文件生成几个 AI 版本，可改成 2、3…
MIN_HUMAN_LINES = 15     # human 代码少于这么多行就跳过
MIN_AI_LINES = 0        # AI 代码少于这么多行就丢弃
MAX_SIMILARITY = 0.80    # 和 human 代码相似度超过这个就丢弃（0~1，越小越严格）
REQUEST_SLEEP = 0.5      # 每次 API 调用后的停顿，避免限流
MAX_TOKENS = 1024        # Grok 输出最大 token 数，大一点就生成更长代码

# =================================================


def read_file(path: str) -> str:
    with io.open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def write_file(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def count_nonempty_lines(code: str) -> int:
    return len([ln for ln in code.splitlines() if ln.strip() != ""])


def build_prompt(human_code: str) -> str:
    """
    构造给 Grok 的 prompt：让它根据人类代码推断题意，然后重新写一个不同结构的解法。
    """
    tmpl = """
    You are an expert competitive programmer using Python 3.

    I will give you a correct Python solution written by a human for some programming problem.
    Your task:

    1. Infer what the problem is asking from the code.
    2. Forget the exact implementation details of the original code.
    3. Write a NEW Python 3 solution for the SAME problem, with these constraints:
       - Do NOT copy any lines or expressions from the original code.
       - Use different variable names and a different structure.
       - If possible, reorganize the logic (e.g., different helper functions or different control flow)
         while staying correct.
       - The solution should be at least {min_lines} non-empty lines of code.
       - The code must be valid Python 3.
    4. Make the code concise but not too dense. You don't need to worry about length of the code.
    Output Python code ONLY. Do not include explanations, comments, or markdown fences.

    Here is the original human-written solution:

    ```python
    {human_code}
    ```
    """
    return textwrap.dedent(tmpl).format(
        min_lines=MIN_AI_LINES,
        human_code=human_code
    )


def call_grok(prompt: str) -> str:
    """
    通过 OpenRouter 调用 Grok 4.1 Fast，返回模型原始输出文本。
    """
    if not OPENROUTER_API_KEY:
        raise RuntimeError("环境变量 OPENROUTER_API_KEY 未设置，请先 setx 之后再运行脚本。")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that writes high-quality Python 3 code."
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": 0.7,
        "top_p": 0.95,
    }

    resp = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=90)
    resp.raise_for_status()
    js = resp.json()

    try:
        return js["choices"][0]["message"]["content"]
    except Exception:
        print("OpenRouter 返回格式异常：", js)
        return ""


def extract_code_from_output(output: str) -> str:
    """
    尝试从模型输出中提取纯代码。
    - 如果包含 ```...``` code block，就只取 block 内部。
    - 否则直接原样返回。
    """
    lines = output.splitlines()
    in_block = False
    buf = []

    for ln in lines:
        striped = ln.strip()
        if not in_block and striped.startswith("```"):
            # 进入 code block
            in_block = True
            continue
        elif in_block and striped.startswith("```"):
            # 退出 code block
            break
        elif in_block:
            buf.append(ln)

    if buf:
        return "\n".join(buf).strip() + "\n"
    else:
        return output.strip() + "\n"


def similarity(a: str, b: str) -> float:
    """
    估计两段代码的相似度（0~1），用 difflib 的 SequenceMatcher。
    """
    return difflib.SequenceMatcher(None, a, b).ratio()


def main():
    print("HUMAN_ROOT:", HUMAN_ROOT)
    print("AI_ROOT   :", AI_ROOT)
    print("MODEL     :", MODEL)

    if not os.path.isdir(HUMAN_ROOT):
        print("错误：HUMAN_ROOT 目录不存在，请先检查路径配置。")
        return

    os.makedirs(AI_ROOT, exist_ok=True)

    meta_f = io.open(METADATA_PATH, "a", encoding="utf-8")

    file_count = 0
    ai_count = 0

    for dirpath, dirnames, filenames in os.walk(HUMAN_ROOT):
        rel_dir = os.path.relpath(dirpath, HUMAN_ROOT)

        for fname in filenames:
            if not fname.endswith(".py"):
                continue

            human_path = os.path.join(dirpath, fname)
            human_code = read_file(human_path)
            human_lines = count_nonempty_lines(human_code)

            if human_lines < MIN_HUMAN_LINES:
                # 太短的人类代码先不生成 AI
                continue

            file_count += 1
            print("=" * 80)
            print(f"[{file_count}] Human file: {human_path} (lines={human_lines})")

            for v in range(VARIANTS_PER_FILE):
                prompt = build_prompt(human_code)

                print(f"  [Variant {v+1}/{VARIANTS_PER_FILE}] 调用 Grok 4.1 Fast...")
                try:
                    raw_output = call_grok(prompt)
                except Exception as e:
                    print("    [ERROR] API 调用失败：", e)
                    time.sleep(2.0)
                    continue

                if not raw_output.strip():
                    print("    [WARN] 空输出，跳过")
                    continue

                ai_code = extract_code_from_output(raw_output)
                ai_lines = count_nonempty_lines(ai_code)

                if ai_lines < MIN_AI_LINES:
                    print(f"    [WARN] AI 代码太短（{ai_lines} 行），跳过")
                    continue

                sim = similarity(human_code, ai_code)
                print(f"    AI lines={ai_lines}, similarity_to_human={sim:.3f}")

                if sim > MAX_SIMILARITY:
                    print("    [WARN] 和人类代码太像，跳过该样本")
                    continue

                # 生成 AI 文件路径（镜像目录结构）
                ai_subdir = rel_dir if rel_dir != "." else ""
                out_dir = os.path.join(AI_ROOT, ai_subdir)
                os.makedirs(out_dir, exist_ok=True)

                base, ext = os.path.splitext(fname)
                ai_fname = f"{base}__grok-4.1-fast__v{v+1}.py"
                ai_path = os.path.join(out_dir, ai_fname)

                write_file(ai_path, ai_code)
                ai_count += 1
                print(f"    [OK] Saved AI code → {ai_path}")

                # 写 metadata
                meta = {
                    "human_path": os.path.relpath(human_path, HUMAN_ROOT),
                    "ai_path": os.path.relpath(ai_path, AI_ROOT),
                    "model": MODEL,
                    "variant": v + 1,
                    "human_lines": human_lines,
                    "ai_lines": ai_lines,
                    "similarity_to_human": sim,
                    "backend": "openrouter",
                    "source_type": "github_leetcode_rewrite_grok",
                }
                meta_f.write(json.dumps(meta, ensure_ascii=False) + "\n")
                meta_f.flush()

                time.sleep(REQUEST_SLEEP)

    meta_f.close()
    print("\nDone.")
    print(f"处理的人类文件数：{file_count}")
    print(f"生成的 AI 文件数：{ai_count}")


if __name__ == "__main__":
    main()

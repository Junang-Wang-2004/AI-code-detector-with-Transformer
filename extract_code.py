import os, json

data = []
for root, _, files in os.walk("leetcode/python"):
    for f in files:
        if f.endswith(".py"):
            path = os.path.join(root, f)
            with open(path, encoding="utf-8", errors="ignore") as fp:
                code = fp.read()
            data.append({
                "source": "human",
                "path": path,
                "code": code
            })

with open("human_code.json", "w", encoding="utf-8") as fp:
    json.dump(data, fp, indent=2, ensure_ascii=False)
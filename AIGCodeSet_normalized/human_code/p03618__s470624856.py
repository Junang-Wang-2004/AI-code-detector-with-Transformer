from collections import Counter
v1 = input().strip()
v2 = len(v1)
v3 = Counter(v1)
v4 = 0
for v5 in v3.values():
    if v5 == 1:
        continue
    v4 += v5 * (v5 - 1) // 2
print(v2 * (v2 - 1) // 2 - v4 + 1)

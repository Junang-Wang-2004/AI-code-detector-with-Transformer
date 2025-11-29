from collections import Counter
v1 = list(input())
v2 = len(v1)
v3 = Counter(v1)
v4 = 1 + v2 * (v2 - 1) // 2
for v5 in v3.values():
    v4 -= v5 * (v5 - 1) // 2
print(v4)

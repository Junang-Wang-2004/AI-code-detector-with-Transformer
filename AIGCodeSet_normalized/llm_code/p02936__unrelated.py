from collections import defaultdict
v1, v2 = map(int, input().split())
v3 = defaultdict(list)
for v4 in range(v1 - 1):
    v5, v6 = map(int, input().split())
    v3[v5].append(v6)
v7 = [0] * (v1 + 1)
v8 = []
for v4 in range(v2):
    v9, v10 = map(int, input().split())
    v8.append((v9, v10))

def f1(a1, a2, a3):
    v7[a1] += a3
    for v1 in v3[a1]:
        if v1 != a2:
            f1(v1, a1, a3)
for v9, v10 in v8:
    f1(v9, -1, v10)
print(*v7[1:])

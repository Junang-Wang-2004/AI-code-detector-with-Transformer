v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v3)]
from collections import defaultdict
v6 = defaultdict(int)
v7 = {i: 0 for v8 in range(10)}
v7[0] = (v1 - 2) * (v2 - 2)
for v9, v10 in v4:
    v9 -= 1
    v10 -= 1
    v11 = max(0, v9 - 2)
    v12 = min(v1 - 3, v9)
    v13 = max(0, v10 - 2)
    v14 = min(v2 - 3, v10)
    for v8 in range(v11, v12 + 1):
        for v15 in range(v13, v14 + 1):
            v7[v6[v8, v15]] -= 1
            v6[v8, v15] += 1
            v7[v6[v8, v15]] += 1
for v8 in range(10):
    print(v7[v8])

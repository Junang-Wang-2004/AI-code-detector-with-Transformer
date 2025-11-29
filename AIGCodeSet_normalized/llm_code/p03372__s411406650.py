import sys
from bisect import bisect_left
v1, v2 = map(int, input().split())
v3 = [tuple(map(int, s.split())) for v4 in sys.stdin.readlines()]
v5 = [x for v6, v7 in v3]
v8, v9, v10 = (0, 0, 0)
for v6, v7 in v3:
    v8 += v7 - (v6 - v9)
    v10 = max(v10, v8)
    v9 = v6
v8, v9, v11 = (0, 0, 0)
for v6, v7 in reversed(v3):
    v6 = v2 - v6
    v8 += v7 - (v6 - v9)
    v11 = max(v11, v8)
    v9 = v6
v12 = bisect_left(v5, v2 // 2)
v8, v9, v13 = (0, 0, 0)
for v14 in range(v12):
    v6, v7 = v3[v14]
    v8 += v7 - (v6 - v9) * 2
    v13 = max(v13, v8)
    v9 = v6
v8, v9, v15 = (0, 0, 0)
for v14 in range(v1 - v12):
    v6, v7 = v3[v1 - 1 - v14]
    v6 = v2 - v6
    v8 += v7 - (v6 - v9)
    v15 = max(v15, v8)
    v9 = v6
v16 = v13 + v15
v8, v9, v15 = (0, 0, 0)
for v14 in range(v1 - v12):
    v6, v7 = v3[v1 - 1 - v14]
    v6 = v2 - v6
    v8 += v7 - (v6 - v9) * 2
    v15 = max(v15, v8)
    v9 = v6
v8, v9, v13 = (0, 0, 0)
for v14 in range(v12):
    v6, v7 = v3[v14]
    v8 += v7 - (v6 - v9)
    v13 = max(v13, v8)
    v9 = v6
v17 = v13 + v15
v12 += 1
v8, v9, v13 = (0, 0, 0)
for v14 in range(v12):
    v6, v7 = v3[v14]
    v8 += v7 - (v6 - v9) * 2
    v13 = max(v13, v8)
    v9 = v6
v8, v9, v15 = (0, 0, 0)
for v14 in range(v1 - v12):
    v6, v7 = v3[v1 - 1 - v14]
    v6 = v2 - v6
    v8 += v7 - (v6 - v9)
    v15 = max(v15, v8)
    v9 = v6
v18 = v13 + v15
v8, v9, v15 = (0, 0, 0)
for v14 in range(v1 - v12):
    v6, v7 = v3[v1 - 1 - v14]
    v6 = v2 - v6
    v8 += v7 - (v6 - v9) * 2
    v15 = max(v15, v8)
    v9 = v6
v8, v9, v13 = (0, 0, 0)
for v14 in range(v12):
    v6, v7 = v3[v14]
    v8 += v7 - (v6 - v9)
    v13 = max(v13, v8)
    v9 = v6
v19 = v13 + v15
print(max([v10, v11, v16, v17, v18, v19]))

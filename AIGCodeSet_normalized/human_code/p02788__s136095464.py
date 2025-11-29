import math
from bisect import bisect_right
v1, v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v4.append((v7, math.ceil(v8 / v3)))
    v5.append(v7)
v4.sort()
v5.sort()
v9 = 0
v10 = 0
v11 = [0] * (v1 + 1)
for v12 in range(v1):
    v7, v8 = v4[v12]
    v9 -= v11[v12]
    if v9 >= v8:
        continue
    else:
        v10 += v8 - v9
        v11[bisect_right(v5, v7 + 2 * v2)] += v8 - v9
        v9 = v8
print(v10)

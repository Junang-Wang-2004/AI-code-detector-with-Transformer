import math
from bisect import bisect_left, bisect_right
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = [False for v3 in range(100001)]
v4[3] = True
v5 = [3]
for v6 in range(5, 100001, 2):
    v7 = True
    v8 = 2
    while v8 < int(math.sqrt(v6)) + 1:
        if v6 % v8 == 0:
            v7 = False
            break
        v8 += 1
    if v7:
        v5.append(v6)
        v4[v6] = True
v9 = []
for v10 in v5:
    if v10 == 3:
        v9.append(v10)
        continue
    v11 = (v10 + 1) // 2
    if v4[v11]:
        v9.append(v10)
for v12, v13 in v2:
    v14 = bisect_right(v9, v13) - bisect_left(v9, v12)
    print(v14)

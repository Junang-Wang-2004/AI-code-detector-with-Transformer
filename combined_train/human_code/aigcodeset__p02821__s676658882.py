from bisect import bisect_left as bl
from itertools import accumulate as ac
v1, v2 = map(int, input().split())
v3 = sorted(list(map(int, input().split())))
v4 = [0] + list(ac(v3[::-1]))
v5, v6 = (2 * v3[-1] * v1 ** 2 + 1, 0)
while v5 - v6 > 1:
    v7 = (v5 + v6) // 2
    v8 = 0
    for v9 in range(v1 - 1, -1, -1):
        if v3[v9] + v3[-1] >= v7:
            v10 = bl(v3, v7 - v3[v9])
            v8 += v1 - v10
        else:
            break
    if v8 < v2:
        v5 = v7
    else:
        v6 = v7
v11, v12 = (0, 0)
v13 = 0
for v9 in range(v1 - 1, -1, -1):
    if v3[v9] + v3[-1] >= v6:
        v14 = bl(v3, v6 - v3[v9])
        v10 = v1 - v14
        v11 += v4[v10] + v10 * v3[v9]
        v13 += v10
    else:
        break
print(v11 - v6 * max(0, v13 - v2))

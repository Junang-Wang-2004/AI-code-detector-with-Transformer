import sys
from itertools import accumulate
v1, v2 = map(int, input().split())
*v3, = map(int, input().split())
v4 = sum(v3)
v5 = []
v6 = []
for v7 in range(1, int(v4 ** 0.5) + 1):
    if v4 % v7 == 0:
        v5.append(v7)
        if v4 // v7 != v7:
            v6.append(v4 // v7)
v6 += v5[::-1]
for v8 in v6:
    v9 = sorted([a % v8 for v10 in v3])
    v11 = sum(v9)
    v12 = tuple(accumulate(v9))
    for v13, v14 in enumerate(v12):
        v15 = v8 * (v1 - v13 - 1) - (v11 - v14)
        if v14 == v15:
            if v14 <= v2:
                print(v8)
                sys.exit()
            else:
                break

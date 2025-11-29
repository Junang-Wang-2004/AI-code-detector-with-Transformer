import numpy as np
from collections import defaultdict
import bisect
v1 = 1000000007
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = defaultdict(list)
for v5, v6 in enumerate(v3):
    v4[v6].append(v5)

def f1(a1, a2, a3, a4):
    v1 = a2 + a3 + a4
    if v1 < 0:
        return 0
    v2 = a1[a2, a3, a4]
    if v2 >= 0:
        return v2
    v3 = v3[v1 - 1] + 1
    v4 = 0
    if v3 == a2:
        v4 += f1(a1, a2 - 1, a3, a4)
        v4 %= v1
    if v3 == a3:
        v4 += f1(a1, a2, a3 - 1, a4)
        v4 %= v1
    if v3 == a4:
        v4 += f1(a1, a2, a3, a4 - 1)
        v4 %= v1
    a1[a2, a3, a4] = v4
    return v4

def f2():
    v1 = [0, 0, 0]
    for v2 in range(v2):
        v3 = len(v4[v2])
        if v3 == 3:
            v1[0] = v1[1] = v1[2] = v2 + 1
        elif v3 == 2:
            v1[0] = v1[1] = v2 + 1
        elif v3 == 1:
            v1[0] = v2 + 1
        else:
            break
    v4 = -np.ones(shape=(v1[0] + 1, v1[1] + 1, v1[2] + 1), dtype=np.int64)
    v4[0, 0, 0] = 1
    v5 = len(v4[0])
    v6 = f1(v4, v1[0], v1[1], v1[2])
    if v5 < 3:
        return 3 * v6 % v1
    else:
        return v6
print(f2())

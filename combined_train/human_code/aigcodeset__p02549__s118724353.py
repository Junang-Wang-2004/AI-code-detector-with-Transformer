import numpy as np
from numba import njit
from numba.types import i8
v1 = np.int64
v2 = 998244353

@njit((i8[:, ::-1], i8[:], i8, i8), cache=True)
def f1(a1, a2, a3, a4):
    v1 = np.ones_like(a2)
    for v2 in range(1, a3):
        v3 = 0
        for v4 in range(a4):
            v5 = v2 - a1[v4, 0]
            if v5 < 0:
                continue
            v6 = v2 - a1[v4, 1] - 1
            v3 += v1[v5] - (v1[v6] if v6 >= 0 else 0)
        a2[v2] = v3 % v2
        v1[v2] = (v1[v2 - 1] + a2[v2]) % v2
    return a2[a3 - 1]

def f2():
    v1 = open(0)
    v2, v3 = [int(x) for v4 in v1.readline().split()]
    v5 = np.fromstring(v1.read(), v1, sep=' ').reshape((-1, 2))
    v6 = np.zeros(v2, v1)
    v6[0] = 1
    v7 = f1(v5, v6, v2, v3)
    print(v7)
f2()

from numba import njit, i8, void
import numpy as np
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = len(input())

@njit(i8(i8), cache=True)
def f1(a1):
    v1, v2, v3, v4 = (np.ones(64, np.int64), 1, 10 ** 9 + 7, 10 ** 9 + 5)
    v1[0] = a1
    for v5 in range(1, 64):
        v1[v5] = v1[v5 - 1] * v1[v5 - 1] % v3
    for v5 in range(64):
        if v4 & 1:
            v2 = v2 * v1[v5] % v3
        v4 >>= 1
    return v2

@njit(void(i8, i8), cache=True)
def f2(a1, a2):
    v1, v2 = (np.ones(a1 + a2 + 1, dtype=np.int64), 10 ** 9 + 7)
    for v3 in range(2, a1 + a2 + 1):
        v1[v3] = v1[v3 - 1] * v3 % v2
    v4 = np.ones(a2 + 1, dtype=np.int64)
    v4[0] = v1[a1 + a2]
    for v3 in range(1, a2 + 1):
        v4[v3] = v4[v3 - 1] * 25 % v2
    v1 = v1[a1 + a2:a1 - 1:-1] * v1[:a2 + 1] % v2
    v5 = 0
    for v3 in range(a2 + 1):
        v5 = (v5 + f1(v1[v3]) * v4[v3]) % v2
    print(v5)
f2(v3, v2)

import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8, i8, i8, i8[:, :]), cache=True)
def f1(a1, a2, a3, a4):
    v1 = np.zeros((a2 + 1, 4), dtype=np.int64)
    for v2 in range(1, a1 + 1):
        v3 = np.zeros((a2 + 1, 4), dtype=np.int64)
        for v4 in range(4):
            v3[:, 0] = np.maximum(v3[:, 0], v1[:, v4])
        v1 = v3
        for v5 in range(1, a2 + 1):
            for v4 in range(4):
                v3[v5][v4] = np.maximum(v3[v5][v4], v3[v5 - 1][v4])
            for v4 in range(2, -1, -1):
                v1[v5, v4 + 1] = np.maximum(v1[v5, v4 + 1], v1[v5, v4] + a4[v2 - 1][v5 - 1])
    v6 = v1[-1].max()
    return v6
v1, v2, v3 = map(int, input().split())
v4 = np.zeros((v1, v2), dtype=np.int64)
for v5 in range(v3):
    v6, v7, v8 = map(int, input().split())
    v4[v6 - 1, v7 - 1] = v8
print(f1(v1, v2, v3, v4))

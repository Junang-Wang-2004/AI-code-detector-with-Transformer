import numpy as np
from numba import njit

@njit
def f1(a1, a2):
    v1 = np.zeros((a1 + 1, a1 + 1), dtype=int)
    for v2 in range(a1):
        for v3 in range(v2 + 1, a1):
            if a2[v2] == a2[v3]:
                if v1[v2][v3] < v3 - v2:
                    v1[v2 + 1][v3 + 1] = v1[v2][v3] + 1
    return np.amax(v1)
v1 = int(input())
v2 = input()
print(f1(v1, v2))

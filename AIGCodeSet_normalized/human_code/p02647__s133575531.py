import numpy as np
from numba import njit
import itertools

@njit
def f1(a1, a2, a3):
    v1 = np.zeros(a1 + 1, dtype=np.int64)
    for v2 in range(a1):
        v3 = a3[v2]
        v4 = max(0, v2 - v3)
        v5 = min(a1, v2 + v3 + 1)
        v1[v4] += 1
        v1[v5] -= 1
    return np.cumsum(v1)[:a1]
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    for v4 in range(v2):
        v3 = f1(v1, v2, v3)
        if v3.min() == v1:
            break
    print(*v3)

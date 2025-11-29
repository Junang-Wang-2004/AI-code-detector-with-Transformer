import sys
import numpy as np
from numba import njit
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines

@njit
def f1(a1):
    v1 = len(a1)
    v2 = np.zeros_like(a1)
    for v3, v4 in enumerate(a1):
        v5 = max(0, v3 - v4)
        v6 = min(v1 - 1, v3 + v4)
        v2[v5] += 1
        if v6 + 1 < v1:
            v2[v6 + 1] -= 1
    v2 = np.cumsum(v2)
    return v2
v4, v5 = map(int, v2().split())
v6 = np.array(v1().split(), np.int64)
v5 = min(v5, 100)
for v7 in range(v5):
    v6 = f1(v6)
print(' '.join(v6.astype(str)))

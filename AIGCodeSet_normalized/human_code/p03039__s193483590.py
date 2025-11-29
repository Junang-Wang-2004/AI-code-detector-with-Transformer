import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)
v1, v2, v3 = map(int, input().split())
v4 = 0
v5 = 10 ** 9 + 7

def f1(a1, a2):
    v1 = len(a1)
    v2 = int(v1 ** 0.5 + 1)
    a1 = np.resize(a1, v2 ** 2).reshape(v2, v2)
    for v4 in range(1, v2):
        a1[:, v4] *= a1[:, v4 - 1]
        a1[:, v4] %= a2
    for v4 in range(1, v2):
        a1[v4] *= a1[v4 - 1, -1]
        a1[v4] %= a2
    return a1.ravel()[:v1]

def f2(a1, a2):
    v1 = np.arange(a1, dtype=np.int64)
    v1[0] = 1
    v2 = f1(v1, a2)
    v1 = np.arange(a1, 0, -1, dtype=np.int64)
    v1[0] = pow(int(v2[-1]), a2 - 2, a2)
    v3 = f1(v1, a2)[::-1]
    return (v2, v3)
v6 = v1 * v2 + 10
v7, v8 = f2(v6, v5)
v7, v8 = (v7.tolist(), v8.tolist())

def f3(a1, a2, a3):
    return v7[a1] * v8[a2] % a3 * v8[a1 - a2] % a3
for v9 in range(1, v1):
    v10 = v1 - v9
    v4 += v9 * v10 * v2 * v2
    v4 %= v5
for v11 in range(1, v2):
    v10 = v2 - v11
    v4 += v11 * v10 * v1 * v1
    v4 %= v5
v4 *= f3(v1 * v2 - 2, v3 - 2, v5)
v4 %= v5
print(v4)

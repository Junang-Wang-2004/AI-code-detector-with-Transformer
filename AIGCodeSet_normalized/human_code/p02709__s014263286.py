import sys
import numpy as np
sys.setrecursionlimit(10 ** 9)
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
for v4 in range(v1):
    v3.append([v2[v4], v4])
v3.sort(reverse=True)
v5 = np.zeros(1, dtype=int)
v6 = np.zeros(1, dtype=int)
for v7, v4 in v3:
    v8 = v5.copy()
    v5 = np.append(v5, [0])
    v9 = len(v8)
    v10 = np.arange((v1 - 1 - v4) * v7, (v1 - 1 - v4) * v7 - v7 * v9, -v7)
    v11 = np.arange(v4 * v7 - v7 * (v9 - 1), (v4 + 1) * v7, v7)
    np.maximum(np.concatenate([v8 + v11, v6]), np.concatenate([v6, v8 + v10]), out=v5)
print(np.max(v5))

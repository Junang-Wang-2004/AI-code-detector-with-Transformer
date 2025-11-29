import sys
import numpy as np
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort(key=lambda x: (x[0], -x[1]))
v5 = np.array([0] * v2)
v6 = 0
for v7, v8 in v3:
    v6 = max(v6, v5[-1] + v8)
    v5[v7:] = np.maximum(v5[:-v7] + v8, v5[v7:])
print(max(v6, v5[-1]))

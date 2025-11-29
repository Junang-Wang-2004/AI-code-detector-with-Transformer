import sys
import numpy as np
v1, v2 = map(int, input().split())
v3 = np.zeros(v2, dtype=np.int64)
v4 = [tuple(map(int, line.split())) for v5 in sys.stdin]
v4.sort()
v6 = 0
for v7, v8 in v4:
    v6 = max(v6, v3.max() + v8)
    v3[v7:] = np.maximum(v3[v7:], v3[:-v7] + v8)
print(max(v6, v3.max()))

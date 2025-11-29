import sys
import numpy as np
v1, v2, *v3 = map(int, sys.stdin.buffer.read().split())
v4 = 998244353
v3 = sorted(v3)
v5 = np.zeros(v2 + 1).astype(np.int64)
v6 = 1
v7 = 0
for v8 in v3:
    if v8 > v2:
        break
    v7 = min(v2, v8 + v7)
    v5[v8 + 1:v7 + 1] = (2 * v5[v8 + 1:v7 + 1] + v5[1:v7 - v8 + 1]) % v4
    v5[v8] = (2 * v5[v8] + v6) % v4
    v5[1:v8] = 2 * v5[1:v8] % v4
    v6 = 2 * v6 % v4
print(v5[v2])

import numpy as np
v1, v2 = map(int, input().split())
v3 = np.array([0] * (v1 + 2))
v4 = np.array([0] * (3 * v1))
v4[1] = 1
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v3[v6] = 1
    v3[v7 + 1] = -1
for v5 in range(1, v1 + 1):
    v3[v5] += v3[v5 - 1]
for v5 in range(1, v1):
    v4[v5] %= 998244353
    v4[v5:v5 + v1 + 2] += v3 * v4[v5]
print(v4[v1] % 998244353)

import numpy as np
v1 = int(input())
v2 = np.empty(v1, dtype=int)
v3 = np.empty(v1, dtype=int)
for v4 in range(v1):
    v2[v4], v3[v4] = [int(d) for v5 in input().split()]
v6 = np.max(np.abs(v2 - v2[1:].reshape(-1, 1)) + np.abs(v3 - v3[1:].reshape(-1, 1)))
print(v6)

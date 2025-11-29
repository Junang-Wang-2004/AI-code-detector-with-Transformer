v1 = int(input())
v2 = list(map(int, input().split()))
import numpy as np
v2 = sorted(v2)
v3 = np.cumsum(v2)
v4 = v1
for v5 in range(v1 - 1):
    if 2 * v3[v5] >= v2[v5 + 1]:
        v4 = min(v5, v4)
    else:
        v4 = v1
print(v1 - v4)

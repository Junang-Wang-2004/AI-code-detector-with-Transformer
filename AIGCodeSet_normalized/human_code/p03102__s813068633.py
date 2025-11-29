import numpy as np
v1, v2, v3 = [int(i) for v4 in input().split()]
v5 = [int(v4) for v4 in input().split()]
v6 = []
for v4 in range(v1):
    v6.append([int(v4) for v4 in input().split()])
v5 = np.array(v5)
v6 = np.array(v6)
print(np.sum(np.sum(v6 * v5, axis=1) + v3 > np.array(0)))

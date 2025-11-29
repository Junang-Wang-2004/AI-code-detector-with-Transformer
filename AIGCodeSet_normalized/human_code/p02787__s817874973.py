import numpy as np
v1, v2 = list(map(int, input().split()))
v3 = []
v4 = []
for v5 in range(v2):
    v6, v7 = list(map(int, input().split()))
    v3.append(v6)
    v4.append(v7)
v3 = np.array(v3)
v4 = np.array(v4)
v8 = np.full(v1 + 1, np.inf)
v8[0] = 0
for v9 in range(1, v1 + 1):
    v8[v9] = np.amin(v8[np.maximum(v9 - v3, 0)] + v4)
print(int(v8[-1]))

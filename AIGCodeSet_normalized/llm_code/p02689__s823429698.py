import numpy as np
v1, v2 = (int(x) for v3 in input().split())
v4 = np.array([int(v3) for v3 in input().split()])
v5 = np.zeros((v1, v1), dtype=bool)
for v6 in range(v2):
    v7, v8 = (int(v3) for v3 in input().split())
    v5[v7 - 1, v8 - 1] = True
    v5[v8 - 1, v7 - 1] = True
v9 = 0
for v10 in range(v1):
    v11 = np.where(v5[v10])[0]
    if np.all(v4[v10] > v4[v11]):
        v9 += 1
print(v9)

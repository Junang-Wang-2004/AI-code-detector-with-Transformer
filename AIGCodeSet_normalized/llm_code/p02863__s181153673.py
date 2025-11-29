import numpy as np
v1, v2 = map(int, input().split())
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7 = map(int, input().split())
    v3.append(v6)
    v4.append(v7)
v8 = np.zeros((v2 + 1, v1 + 1))
for v9 in range(v3[0], v2 + 1):
    v8[v9, 1] = v4[0]
for v10 in range(2, v1 + 1):
    for v9 in range(v2 + 1):
        if v3[v10 - 1] <= v9:
            v8[v9, v10] = max(v8[v9, v10 - 1], v8[v9 - v3[v10 - 1], v10 - 1] + v4[v10 - 1])
        else:
            v8[v9, v10] = v8[v9, v10 - 1]
print(v8[v2, v1])

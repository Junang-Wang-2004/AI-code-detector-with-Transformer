import numpy as np
v1, v2, v3 = list(map(int, input().split()))
v4 = [list(map(int, list(input()))) for v5 in range(v1)]
v6 = np.array(v4)
v7 = v1 * v2
for v8 in range(2 ** (v1 - 1)):
    v4 = np.copy(v6)
    v9 = []
    for v10 in range(v1 - 1):
        if v8 >> v10 & 1:
            v9.append(v10 + 1)
    if len(v9) > v7:
        continue
    v11 = np.vsplit(v4, v9)
    v11 = np.array([np.sum(row, axis=0) for v12 in v11])
    v13 = np.hstack([np.zeros((v11.shape[0], 1), dtype=np.uint32), np.cumsum(v11, 1)])
    v14 = len(v9)
    v15 = 0
    for v16 in range(v2 + 1):
        if (v13[:, v16] - v13[:, v15] > v3).any():
            v15 = v16
            v14 += 1
            if v14 > v7:
                continue
    v7 = min([v14, v7])
print(v7)

v1, v2 = map(int, input().split())
v3 = 10 ** 5
v4 = [[0] * (v3 + 1) for v5 in range(v2 + 1)]
v6 = []
for v5 in range(v1):
    v6.append(list(map(int, input().split())))
v6 = sorted(v6, key=lambda x: x[0])
v6 = sorted(v6, key=lambda x: x[2])
for v7 in range(v1):
    v8, v9, v10 = (v6[v7][0], v6[v7][1], v6[v7][2])
    try:
        if v6[v7 - 1][2] == v10 and v6[v7 - 1][1] == v8:
            v4[v10][v8 + 1] += 1
        else:
            v4[v10][v8] += 1
    except IndexError:
        v4[v10][v8] += 1
    if v9 + 1 <= v3:
        v4[v10][v9 + 1] -= 1
for v10 in range(v2 + 1):
    for v7 in range(1, v3 + 1):
        v4[v10][v7] += v4[v10][v7 - 1]
import numpy as np
print(np.max(np.sum(v4, axis=0)))

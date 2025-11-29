import numpy as np
v1, v2 = list(map(int, input().split()))
v3 = 10 ** 5
v4 = [i for v5 in range(v3)]
v4[1] = 0
for v5 in range(2, v3):
    v6 = v5 * v5
    if v4[v6] == 0 or v6 > v3:
        break
    while v6 < v3:
        v4[v6] = 0
        v6 += v5
v4 = np.array(v4)
v4 = v4[v4 != 0]
v7 = {}
for v8 in v4:
    while v2 % v8 == 0:
        if v7.get(v8, 0) == 0:
            v7[v8] = 1
        else:
            v7[v8] += 1
        v2 /= v8
    if v2 == 1:
        break
v9 = 1
for v8 in v7.values():
    v10 = []
    v11 = []
    for v5 in range(v8, 0, -1):
        v10.append(v5 + v1 - 1)
        v11.append(v5)
    for v5, v12 in enumerate(v10):
        for v13, v14 in enumerate(v11):
            if v10[v5] % v11[v13] == 0:
                v10[v5] /= v11[v13]
                v11[v13] = 1.0
    for v12 in v10:
        v9 *= v12
        v9 %= 10 ** 9 + 7
print(int(v9))

v1, v2, v3 = map(int, input().split())
v4 = []
v5 = 0
v6 = 0
v7 = 0
for v8 in range(v1):
    v9, v10, v11 = map(int, input().split())
    v4.append((v9, v10, v11))
    v5 += v9
    v6 += v10
    v7 += v11
v12 = [[float('infinity')] * (v5 + 1) for v8 in range(v6 + 1)]
v12[0][0] = 0
for v9, v10, v11 in v4:
    v12[v10][v9] = v11
for v9, v10, v11 in v4:
    for v13 in range(1, v6 + 1):
        for v14 in range(1, v5 + 1):
            if v14 - v9 > 0 and v13 - v10 > 0:
                v12[v13][v14] = min(v12[v13][v14], v12[v13 - v10][v14 - v9] + v11)
v15 = float('infinity')
for v16 in range(1, v6 + 1):
    for v17 in range(1, v5 + 1):
        if v12[v16][v17] == float('infinity'):
            continue
        if v2 * v12[v16] == v12[v17] * v3:
            v15 = min(v15, v12[v16][v17])
if v15 == float('infinity'):
    print(-1)
else:
    print(v15)

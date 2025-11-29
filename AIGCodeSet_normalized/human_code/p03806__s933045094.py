v1, v2, v3 = map(int, input().split())
v4, v5, v6 = ([], [], [])
for v7 in range(v1):
    v8, v9, v10 = map(int, input().split())
    v4.append(v8)
    v5.append(v9)
    v6.append(v10)
v11 = float('inf')
v12 = [[[v11] * 401 for v7 in range(401)] for v13 in range(v1 + 1)]
v12[0][0][0] = 0
for v7 in range(1, v1 + 1):
    for v14 in range(401):
        for v15 in range(401):
            if v14 - v4[v7 - 1] >= 0 and v15 - v5[v7 - 1] >= 0:
                v12[v7][v14][v15] = min(v12[v7][v14][v15], v12[v7 - 1][v14][v15], v12[v7 - 1][v14 - v4[v7 - 1]][v15 - v5[v7 - 1]] + v6[v7 - 1])
            else:
                v12[v7][v14][v15] = min(v12[v7][v14][v15], v12[v7 - 1][v14][v15])
v16 = v11
for v7 in range(1, 401):
    v17 = v2 * v7
    v18 = v3 * v7
    if v17 > 400 or v18 > 400:
        break
    v16 = min(v16, v12[v1][v17][v18])
print(v16 if v16 != v11 else -1)

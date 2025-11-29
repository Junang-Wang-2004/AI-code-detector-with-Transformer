v1, v2, v3 = map(int, input().split())
v4 = [[0] * 401 for v5 in range(401)]
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split())
    for v9 in range(400, -1, -1):
        for v10 in range(400, -1, -1):
            if v9 - v6 < 0 or v10 - v7 < 0:
                continue
            elif v4[v9 - v6][v10 - v7] == 0:
                continue
            elif v4[v9][v10] == 0:
                v4[v9][v10] = v4[v9 - v6][v10 - v7] + v8
            else:
                v4[v9][v10] = min(v4[v9][v10], v4[v9 - v6][v10 - v7] + v8)
    if v4[v6][v7] == 0:
        v4[v6][v7] = v8
    else:
        v4[v6][v7] = min(v4[v6][v7], v8)
v11 = 10 ** 10
for v9 in range(401):
    if v9 * v2 > 400 or v9 * v3 > 400:
        break
    if v4[v9 * v2][v9 * v3] == 0:
        continue
    else:
        v11 = min(v11, v4[v9 * v2][v9 * v3])
if v11 == 10 ** 10:
    print(-1)
else:
    print(v11)

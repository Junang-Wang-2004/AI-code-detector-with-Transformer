v1, v2, v3 = map(int, input().split())
v4 = [input() for v5 in range(v1)]
v6 = [[-1] * v2 for v5 in range(v1)]
v7 = []
v8 = 1
for v9 in range(v1):
    v10 = v4[v9]
    for v11 in range(v2):
        if v10[v11] == '#':
            v6[v9][v11] = v8
            v8 += 1
            v7.append((v9, v11))
for v12 in v7:
    v9, v11 = v12
    v8 = v6[v9][v11]
    v13, v14 = (v9 - 1, v11 - 1)
    v15 = v11 + 1
    while v13 > -1:
        if v6[v13][v11] != -1:
            break
        v13 -= 1
    v13 += 1
    while v14 > -1:
        if v6[v9][v14] != -1:
            break
        v14 -= 1
    v14 += 1
    while v15 < v2:
        if v6[v9][v15] != -1:
            break
        v15 += 1
    v15 -= 1
    for v14 in range(v13, v9 + 1):
        v16 = v6[v14]
        for v17 in range(v14, v15):
            v16[v17] = v8
for v18 in range(v1 - 1, -1, -1):
    if v6[v18][0] != -1:
        break
v18 += 1
if v18 != v1:
    for v9 in range(v18, v1):
        v19 = v6[v9 - 1]
        v20 = v6[v9]
        for v11 in range(v2):
            v20[v11] = v19[v11]
for v9 in range(v1):
    v20 = v6[v9]
    for v21 in range(v2 - 1, -1, -1):
        if v20[v21] != -1:
            break
    v21 += 1
    if v21 != v2:
        v8 = v20[v21 - 1]
        for v11 in range(v21, v2):
            v20[v11] = v8
for v9 in range(v1):
    print(*v6[v9])

v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
v6 = []
v7 = []
v8 = []
for v9 in range(v1):
    for v10 in range(v1):
        v5[v9][v10] -= 1
        if (v9 + v10) % 3 == 0:
            v6.append(v5[v9][v10])
        if (v9 + v10) % 3 == 1:
            v7.append(v5[v9][v10])
        if (v9 + v10) % 3 == 2:
            v8.append(v5[v9][v10])
for v11 in range(v2):
    for v9 in range(v2):
        for v10 in range(v2):
            v3[v9][v10] = min(v3[v9][v10], v3[v9][v11] + v3[v11][v10])
v12 = float('inf')
for v13 in range(v2):
    for v14 in range(v2):
        if v13 == v14:
            continue
        for v15 in range(v2):
            if v13 == v15 or v14 == v15:
                continue
            v16 = 0
            v16 += sum((v3[clr_g1][v13] for v17 in v6))
            v16 += sum((v3[clr_g2][v14] for v18 in v7))
            v16 += sum((v3[clr_g3][v15] for v19 in v8))
            v12 = min(v12, v16)
print(v12)

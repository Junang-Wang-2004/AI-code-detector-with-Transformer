v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = [[0] * v1 for v4 in range(8)]
for v6, v7 in enumerate(v3):
    v8, v9, v10 = v7
    v5[0][v6] = v8 + v9 + v10
    v5[1][v6] = v8 + v9 - v10
    v5[2][v6] = v8 - v9 + v10
    v5[3][v6] = v8 - v9 - v10
    v5[4][v6] = -v8 + v9 + v10
    v5[5][v6] = -v8 + v9 - v10
    v5[6][v6] = -v8 - v9 + v10
    v5[7][v6] = -v8 - v9 - v10
v11 = [0] * 8
for v4 in range(8):
    v5[v4].sort()
    v11[v4] = sum(v5[v4][-v2:])
print(max(v11))

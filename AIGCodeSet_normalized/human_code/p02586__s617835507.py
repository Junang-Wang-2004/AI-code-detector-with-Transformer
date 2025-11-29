v1, v2, v3 = map(int, input().split())
v4 = [[[0, 0, 0, 0] for v5 in range(v2 + 1)] for v6 in range(2)]
v7 = [[0] * (v2 + 1) for v6 in range(v1)]
for v6 in range(v3):
    v8, v9, v10 = map(int, input().split())
    v7[v8 - 1][v9 - 1] = v10
for v11 in range(v1):
    for v12 in range(v2):
        v4[1][v12][0] = max(v4[0][v12])
        v4[1][v12][1] = max(v4[1][v12][0] + v7[v11][v12], v4[1][v12 - 1][1], v4[1][v12 - 1][0] + v7[v11][v12])
        v4[1][v12][2] = max(v4[1][v12 - 1][2], v4[1][v12 - 1][1] + v7[v11][v12])
        v4[1][v12][3] = max(v4[1][v12 - 1][3], v4[1][v12 - 1][2] + v7[v11][v12])
    v4[0] = v4[1][:]
print(max(v4[1][v2 - 1]))

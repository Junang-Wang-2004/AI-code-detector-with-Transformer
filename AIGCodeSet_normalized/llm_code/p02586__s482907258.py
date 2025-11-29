v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v3)]
v6 = [[0 for v5 in range(v2 + 1)] for v5 in range(v1 + 1)]
for v7, v8, v9 in v4:
    v6[v7][v8] = v9
v10 = [[[0 for v5 in range(4)] for v5 in range(v2 + 1)] for v5 in range(v1 + 1)]
for v11 in range(1, v1 + 1):
    for v12 in range(1, v2 + 1):
        for v13 in range(4):
            if v13 < 3:
                v10[v11][v12][v13 + 1] = max(v10[v11 - 1][v12][v13 + 1], v10[v11][v12 - 1][v13 + 1], v10[v11 - 1][v12][v13] + v6[v11][v12], v10[v11][v12 - 1][v13] + v6[v11][v12])
            else:
                v10[v11][v12][v13] = max(v10[v11 - 1][v12][v13], v10[v11][v12 - 1][v13], v10[v11 - 1][v12][v13 - 1] + v6[v11][v12], v10[v11][v12 - 1][v13 - 1] + v6[v11][v12])
print(max(v10[v1][v2]))

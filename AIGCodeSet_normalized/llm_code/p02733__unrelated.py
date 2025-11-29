v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input())) for v5 in range(v1)]
v6 = [sum(row) for v7 in v4]
v8 = [sum((v4[i][j] for v9 in range(v1))) for v10 in range(v2)]
v11 = max(max(v6) // v3 - 1, max(v8) // v3 - 1)
print(v11)

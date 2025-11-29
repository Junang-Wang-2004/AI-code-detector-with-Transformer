v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = sum((1 for v5 in v3 if v5 % 2 == 0))
v6 = v1 - v4
v7 = [[0] * (v6 + 1) for v8 in range(v4 + 1)]
v7[0][0] = 1
for v5 in v3:
    if v5 % 2 == 0:
        for v9 in range(v4, 0, -1):
            for v10 in range(v6 + 1):
                v7[v9][v10] += v7[v9 - 1][v10]
    else:
        for v9 in range(v4 + 1):
            for v10 in range(v6, 0, -1):
                v7[v9][v10] += v7[v9][v10 - 1]
print(v7[v4][v6] if v2 == 0 else v7[v4][v6 - 1])

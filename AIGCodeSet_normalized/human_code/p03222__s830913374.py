v1, v2, v3 = map(int, input().split())
v4 = [[0] * v2 for v5 in range(v1 + 1)]
v6 = 1000000007
v4[0][v3 - 1] = 1
v7 = [1, 1, 2, 3, 5, 8, 13, 21]
for v5 in range(v1):
    for v8 in range(v2):
        if v8 != 0:
            if v8 == v2 - 1 or v8 == 1:
                v4[v5 + 1][v8] += v4[v5][v8 - 1] * v7[v2 - 2] % v6
            else:
                v4[v5 + 1][v8] += v4[v5][v8 - 1] * (v7[v8 - 1] * v7[v2 - 1 - v8]) % v6
        if v8 != v2 - 1:
            if v8 == 0 or v8 == v2 - 2:
                v4[v5 + 1][v8] += v4[v5][v8 + 1] * v7[v2 - 2] % v6
            else:
                v4[v5 + 1][v8] += v4[v5][v8 + 1] * (v7[v8] * v7[v2 - 2 - v8]) % v6
        if v8 == 0 or v8 == v2 - 1:
            v4[v5 + 1][v8] += v4[v5][v8] * v7[v2 - 1] % v6
        else:
            v4[v5 + 1][v8] += v4[v5][v8] * (v7[v8] * v7[v2 - 1 - v8]) % v6
print(v4[v1][0] % v6)

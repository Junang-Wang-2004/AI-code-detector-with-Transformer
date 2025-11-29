v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
if v2 == 1:
    print(1)
else:
    v5 = [1, 2, 3, 5, 8, 13, 21, 34, 1, 1, 1]
    v6 = [[0 for v7 in range(v2)] for v7 in range(v1 + 1)]
    v6[0][0] = 1
    for v8 in range(0, v1):
        for v9 in range(v2):
            if v9 != 0 and v9 != v2 - 1:
                v6[v8 + 1][v9] = v5[v9 - 1] * v5[v2 - 2 - v9] * v6[v8][v9] + v5[v9 - 2] * v5[v2 - 2 - v9] * v6[v8][v9 - 1] + v5[v9 - 1] * v5[v2 - 3 - v9] * v6[v8][v9 + 1]
            elif v9 == 0:
                v6[v8 + 1][v9] = v5[v9 - 1] * v5[v2 - 2 - v9] * v6[v8][v9] + v5[v9 - 1] * v5[v2 - 3 - v9] * v6[v8][v9 + 1]
            else:
                v6[v8 + 1][v9] = v5[v9 - 1] * v5[v2 - 2 - v9] * v6[v8][v9] + v5[v9 - 2] * v5[v2 - 2 - v9] * v6[v8][v9 - 1]
            v6[v8 + 1][v9] %= v4
    print(v6[v1][v3 - 1])

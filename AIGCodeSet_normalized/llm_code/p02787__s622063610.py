import math
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v2)]
v5 = [[[float('INF'), 0] for v4 in range(v1 + 1)] for v6 in range(v2 + 1)]
v5[0] = [[0, 0] for v4 in range(v1 + 1)]
for v6 in range(1, v2 + 1):
    v7 = v3[v6 - 1][0]
    v8 = v3[v6 - 1][1]
    for v9 in range(1, v1 + 1):
        v10 = math.floor(v9 / v7) + 1
        for v11 in range(v10):
            v12 = v5[v6 - 1][v9 - v7 * v11][0] + v8 * v11
            v13 = v5[v6 - 1][v9 - v7 * v11][1] + v7 * v11
            if v13 >= v9:
                if v5[v6][v9][0] > v12:
                    v5[v6][v9] = [v12, v13]
print(v5[v2][v1][0])

v1, v2, v3 = map(int, input().split())
v4 = [list(map(int, input().split())) for v5 in range(v2)]
v6 = int(input())
v7 = [list(map(int, input().split())) for v5 in range(v6)]
v8 = [[10 ** 17] * v1 for v5 in range(v1)]
for v5 in range(v2):
    if v4[v5][2] <= v3:
        v8[v4[v5][0] - 1][v4[v5][1] - 1] = v4[v5][2]
        v8[v4[v5][1] - 1][v4[v5][0] - 1] = v4[v5][2]
for v5 in range(v1):
    for v9 in range(v1):
        for v10 in range(v1):
            v8[v9][v10] = min(v8[v9][v10], v8[v9][v5] + v8[v5][v10])
for v5 in range(v6):
    if v8[v7[v5][0] - 1][v7[v5][1] - 1] <= 10 * 18:
        print(v8[v7[v5][0] - 1][v7[v5][1] - 1] // v3)
    else:
        print(-1)

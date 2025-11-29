v1, v2 = map(int, input().split())
v3 = [int(c) for v4 in input().split()]
v5 = [int(v4) for v4 in input().split()]
v6 = 10 ** 9 + 7
v7 = [[0] * (v2 + 1) for v8 in range(v1 + 1)]
v9 = [[0] * (v2 + 1) for v8 in range(v1 + 1)]
v7[0][0] = 1
for v8 in range(v1 + 1):
    v9[v8][0] = 1
for v10 in range(v2 + 1):
    v9[0][v10] = 1
for v8 in range(v1):
    for v10 in range(v2):
        if v3[v8] != v5[v10]:
            v7[v8 + 1][v10 + 1] = 0
        else:
            v7[v8 + 1][v10 + 1] = v9[v8][v10]
        v9[v8 + 1][v10 + 1] = v9[v8][v10 + 1] + v9[v8 + 1][v10] - v9[v8][v10] + v7[v8 + 1][v10 + 1]
        v9[v8 + 1][v10 + 1] %= v6
print(v9[-1][-1])

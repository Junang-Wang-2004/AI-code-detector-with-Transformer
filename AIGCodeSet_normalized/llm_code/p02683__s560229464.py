v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v6 = [int(v3) for v3 in input().split()]
    v4.append(v6)
v7 = [[float('inf')] * (v3 + 1) for v5 in range(v2 + 1)]
v7[0][0] = 0
for v8 in range(v1):
    for v9 in range(v2, -1, -1):
        for v10 in range(v3 + 1):
            if v10 >= v4[v8][0]:
                v7[v9 + 1][v10] = min(v7[v9 + 1][v10], v7[v9][v10 - v4[v8][0]] + v4[v8][0])
            if v9 > 0 and v10 + v4[v8][v9 + 1] <= v3:
                v7[v9 + 1][v10 + v4[v8][v9 + 1]] = min(v7[v9 + 1][v10 + v4[v8][v9 + 1]], v7[v9][v10] + v4[v8][0])
v11 = v7[v2][v3]
if v11 == float('inf'):
    print(-1)
else:
    print(v11)

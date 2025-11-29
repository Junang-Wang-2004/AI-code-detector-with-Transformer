v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort(key=lambda x: x[0] / x[1], reverse=True)
v5 = [[0 for v4 in range(v2 + 1)] for v6 in range(v1 + 1)]
for v4 in range(1, v1 + 1):
    for v6 in range(1, v2 + 1):
        if v6 - v3[v4 - 1][0] >= 0:
            v5[v4][v6] = max(v5[v4 - 1][v6], v5[v4 - 1][v6 - v3[v4 - 1][0]] + v3[v4 - 1][1])
        else:
            v5[v4][v6] = v5[v4 - 1][v6]
v7 = v5[v1][v2]
print(v7)

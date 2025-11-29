v1, v2 = map(int, input().split())
v3 = [[0] * v1 for v4 in range(8)]
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split())
    v3[0][v5] = v6 + v7 + v8
    v3[1][v5] = v6 + v7 - v8
    v3[2][v5] = v6 - v7 + v8
    v3[3][v5] = v6 - v7 - v8
    v3[4][v5] = -v6 + v7 + v8
    v3[5][v5] = -v6 + v7 - v8
    v3[6][v5] = -v6 - v7 + v8
    v3[7][v5] = -v6 - v7 - v8
print(max((sum(sorted(v3[v5])[-v2:]) for v5 in range(8))) if v2 != 0 else 0)

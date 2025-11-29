v1, v2 = map(int, input().split())
v3 = [[10 ** 9] * 2 ** v1 for v4 in range(v2 + 1)]
v3[0][0] = 0
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v8 = list(map(int, input().split()))
    v9 = 0
    for v10 in v8:
        v9 |= 1 << v10 - 1
    for v11 in range(2 ** v1):
        v12 = v5 + 1
        v13 = v11 | v9
        v3[v12][v11] = min(v3[v12][v11], v3[v5][v11])
        v3[v12][v13] = min(v3[v12][v13], v3[v5][v11] + v6)
print(v3[v2][2 ** v1 - 1])

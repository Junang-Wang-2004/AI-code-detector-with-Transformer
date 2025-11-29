v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 998244353
v5 = [[0] * (v2 + 1) for v6 in range(v1 + 1)]
v5[0][0] = 1
for v7 in range(v1):
    v8 = v3[v7]
    for v9 in range(v2 + 1):
        v5[v7 + 1][v9] = 2 * v5[v7][v9]
        if v9 - v8 >= 0:
            v5[v7 + 1][v9] += v5[v7][v9 - v8]
        v5[v7 + 1][v9] %= v4
print(v5[-1][-1])

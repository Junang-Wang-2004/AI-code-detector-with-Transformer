v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 998244353
v5 = [[0] * (v2 + 1) for v6 in range(v1 + 1)]
v5[0][0] = 1
for v6 in range(v1):
    for v7 in range(v2 + 1):
        v5[v6 + 1][v7] += v5[v6][v7] * 2 % v4
        if v7 - v3[v6] >= 0:
            v5[v6 + 1][v7] += v5[v6][v7 - v3[v6]]
        v5[v6 + 1][v7] %= v4
print(v5[-1][-1])

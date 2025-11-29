v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [[0] * (v2 + 1) for v5 in range(v1 + 1)]
for v6 in range(v1 + 1):
    for v7 in range(v2 + 1):
        if v7 == 0:
            v4[v6][v7] = 1
        else:
            v4[v6][v7] = 0
for v6 in range(1, v1 + 1):
    v8 = v3[v6 - 1]
    for v7 in range(v2 + 1):
        if v8 <= v2 and v7 >= v8:
            v4[v6][v7] = (v4[v6 - 1][v7] + v4[v6 - 1][v7 - v8]) % 998244353
        else:
            v4[v6][v7] = v4[v6 - 1][v7]
print(v4[v1][v2])

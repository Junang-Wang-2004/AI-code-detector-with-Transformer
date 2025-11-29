v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 998244353
v5 = pow(2, v4 - 2, v4)
v6 = [0 for v7 in range(3001)]
v6[0] = 1
for v7 in range(v1):
    for v8 in range(3000, -1, -1):
        if v8 >= v3[v7]:
            v6[v8] = v5 * v6[v8 - v3[v7]] + v6[v8]
            v6[v8] %= v4
v9 = pow(2, v1, v4) * v6[v2]
v9 %= v4
print(v9)

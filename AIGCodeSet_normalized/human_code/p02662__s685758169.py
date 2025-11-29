v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v5 = 998244353
v6 = [0] * (v2 + 1)
v6[0] = 1
for v7 in v3:
    for v4 in range(v2, -1, -1):
        if v4 >= v7:
            v6[v4] = v6[v4] * 2 + v6[v4 - v7]
        else:
            v6[v4] = v6[v4] * 2
        v6[v4] %= v5
print(v6[-1])

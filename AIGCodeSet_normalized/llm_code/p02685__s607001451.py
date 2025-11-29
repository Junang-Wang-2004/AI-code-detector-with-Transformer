v1, v2, v3 = map(int, input().split())
v4 = 998244353
v5 = v2 * pow(v2 - 1, v1 - 1, v4) % v4
v6 = 1
for v7 in range(1, v3 + 1):
    v6 = v6 * (v1 - v7) // v7
    v6 = v6 % v4
    v5 += v2 * v6 % v4 * pow(v2 - 1, v1 - 1 - v7, v4) % v4
    v5 = v5 % v4
print(v5)

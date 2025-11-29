v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = 0
v6 = 0
v7, v8 = (10 ** 9 + 7, 998244353)
v9 = v7
for v10 in range(1, v1):
    v5 = (v5 + v10 * (v3[v10] - v3[v10 - 1]) % v9) % v9
    v6 = (v6 + v5) % v9
v11 = 0
v12 = 0
for v10 in range(1, v2):
    v11 = (v11 + v10 * (v4[v10] - v4[v10 - 1]) % v9) % v9
    v12 = (v12 + v11) % v9
print(v6 * v12 % v9)

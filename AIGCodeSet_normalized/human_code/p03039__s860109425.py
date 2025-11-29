v1 = 10 ** 9 + 7
v2, v3, v4 = map(int, input().split())
v5 = [0] * (v4 + 3)
v5[1] = 1
for v6 in range(2, v4 + 2):
    v5[v6] = (v1 - v1 // v6) * v5[v1 % v6] % v1
v7 = (v2 * v2 * (v3 + 1) * v3 * (v3 - 1) + v3 * v3 * (v2 + 1) * v2 * (v2 - 1)) // 6
for v6 in range(v4 - 2):
    v7 = v7 * (v2 * v3 - 2 - v6) * v5[v6 + 1] % v1
print(v7)

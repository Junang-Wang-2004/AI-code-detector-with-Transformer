v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7
v5, v6 = (0, 0)
for v7 in range(v1):
    for v8 in range(v1):
        v5 += abs(v7 - v8)
        v5 %= v4
v5 = v5 * v2 ** 2 % v4
for v7 in range(v2):
    for v8 in range(v2):
        v6 += abs(v7 - v8)
        v6 %= v4
v6 = v6 * v1 ** 2 % v4
v9 = (v5 + v6) // 2
v10 = [1 for v11 in range(v1 * v2)]
for v7 in range(1, v1 * v2):
    v10[v7] = v10[v7 - 1] * v7 % v4
v9 = v9 * v10[v1 * v2 - 2] * pow(v10[v3 - 2], v4 - 2, v4) * pow(v10[v1 * v2 - v3], v4 - 2, v4) % v4
print(v9)

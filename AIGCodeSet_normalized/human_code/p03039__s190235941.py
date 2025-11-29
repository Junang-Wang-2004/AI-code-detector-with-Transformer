v1 = 10 ** 9 + 7
v2, v3, v4 = [int(item) for v5 in input().split()]
v6 = 1
for v7 in range(2, v4):
    v6 = v6 * (v2 * v3 - v7) % v1
for v7 in range(1, v4 - 2 + 1):
    v6 = v6 * pow(v7, v1 - 2, v1) % v1
print(v6 * (v3 ** 2 * v2 * (v2 ** 2 - 1) // 6 + v2 * (v2 - 1) * v3 * (v3 ** 2 - 1) // 6 + v2 * v3 * (v3 ** 2 - 1) // 6) % v1)

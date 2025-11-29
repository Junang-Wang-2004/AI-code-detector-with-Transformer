v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4, v5 = (0, 0)
for v6 in range(v2 - 1, v1 + 1):
    v4 += v6 * (v6 + 1) // 2 - 1
    v5 += v1 * (v1 + 1) // 2 - (v1 - v6 - 1) * (v1 - v6) // 2
v7 = (v5 - v4) % v3
print(v7)

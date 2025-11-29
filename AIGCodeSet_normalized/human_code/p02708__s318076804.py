v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v2, v1 + 2):
    v5 = v4 * (v4 - 1) // 2
    v6 = v4 * v1 - v5
    v3 = v3 + (v6 - v5 + 1)
print(v3 % (10 ** 9 + 7))

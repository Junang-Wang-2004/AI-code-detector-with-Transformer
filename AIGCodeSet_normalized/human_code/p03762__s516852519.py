v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
v4 = tuple(map(int, input().split()))
v5 = tuple(map(int, input().split()))
v6, v7 = (0, 0)
for v8 in range(v2):
    v6 += v8 * v4[v8] - (v2 - v8 - 1) * v4[v8]
    v6 %= v1
for v8 in range(v3):
    v7 += v8 * v5[v8] - (v3 - v8 - 1) * v5[v8]
    v7 %= v1
print(v6 * v7 % v1)

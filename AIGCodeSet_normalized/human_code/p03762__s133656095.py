v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = int(1000000000.0) + 7
v6 = 0
for v7 in range(v1):
    v6 += (2 * v7 + 1 - v1) * v3[v7]
    v6 %= v5
v8 = 0
for v9 in range(v2):
    v8 += (2 * v9 + 1 - v2) * v4[v9]
    v8 %= v5
print(v6 * v8 % v5)

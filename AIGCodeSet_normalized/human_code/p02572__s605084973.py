v1 = 10 ** 9 + 7
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = [0] * (v2 + 1)
for v5 in range(v2 - 1, 0, -1):
    v4[v5] = (v3[v5] + v4[v5 + 1]) % v1
v6 = 0
for v5 in range(v2 - 1):
    v7 = v3[v5] * v4[v5 + 1] % v1
    v6 += v7
    v6 %= v1
print(v6)

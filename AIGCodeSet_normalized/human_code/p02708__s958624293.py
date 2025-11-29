v1, v2 = map(int, input().split())
v3 = 0
v4 = list(range(v1 + 1))
v5 = [0]
for v6 in range(v1 + 1):
    v5.append(v5[v6] + v4[v6])
v7 = 10 ** 9 + 7
for v6 in range(v2, v1 + 2):
    v8 = v5[-1] - v5[-v6 - 1] - v5[v6] + v5[0] + 1
    v3 += v8
    v3 %= v7
print(v3)

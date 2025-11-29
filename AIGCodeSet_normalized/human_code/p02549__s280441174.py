v1, v2 = map(int, input().split())
v3 = 998244353
v4 = []
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v4.append((v6, v7))
v8 = [0] * (v1 + 10)
v8[1] = 1
for v9 in range(0, v1):
    if v8[v9] == 0:
        continue
    for v6, v7 in v4:
        if v9 + v6 > v1 + 1:
            continue
        v8[v9 + v6] += v8[v9]
        if v9 + v7 - 1 > v1 + 1:
            continue
        v8[v9 + v7 + 1] -= v8[v9]
    v8[v9 + 1] += v8[v9]
    v8[v9 + 1] %= v3
print((v8[v1] - v8[v1 - 1]) % v3)

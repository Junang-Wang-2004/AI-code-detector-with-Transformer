v1, v2 = map(int, input().split())
v3 = input().split()
v4 = input().split()
v5 = [[0] * (v1 + 2) for v6 in range(v2 + 2)]
for v7 in range(v1 + 1):
    v5[v7][0] = 1
for v8 in range(v2 + 1):
    v5[0][v8] = 1
for v7, v9 in enumerate(v3, 1):
    for v8, v10 in enumerate(v4, 1):
        v5[v7][v8] += v5[v7 - 1][v8]
        v5[v7][v8] += v5[v7][v8 - 1]
        if v9 == v10:
            v5[v7][v8] += v5[v7 - 1][v8 - 1]
        v5[v7][v8] -= v5[v7 - 1][v8 - 1]
        v5[v7][v8] %= mod
print(v5[v1][v2])

def f1(a1, a2, a3):
    v1, v2 = (-1, a1)
    while v2 - v1 > 1:
        if a2[(v1 + v2) // 2] > a3:
            v2 = (v1 + v2) // 2
        else:
            v1 = (v1 + v2) // 2
    return v2 + 1
v1, v2, v3 = map(int, input().split())
v4 = sorted((list(map(int, input().split())) for v5 in range(v1)))
v6 = [i for v7, v8 in v4]
v9 = [(v8 + v3 - 1) // v3 for v7, v8 in v4]
v10, v11, v12 = ([0] * (v1 + 1), [0] * (v1 + 1), 0)
for v7 in range(v1):
    v8 = f1(v1, v6, v6[v7] + 2 * v2) - 1
    v13 = max(v9[v7] - (v11[v7 - 1] + v10[v7]), 0)
    v10[v7] += v13
    v10[v8] -= v13
    v11[v7] += v11[v7 - 1] + v10[v7]
    v12 += v13
print(v12)

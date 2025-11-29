from itertools import product
v1, v2 = map(int, input().split())
v3, v4 = zip(*[map(int, input().split()) for v5 in range(v1)])
v6 = 10 ** 18
v7 = v6
for v8 in product((0, 1), repeat=v1):
    v9 = list(v3)
    v10 = 0
    v11 = 0
    for v12 in range(v1):
        if v8[v12]:
            v11 += v4[v12]
            v11 += v3[v12] * 100 * (v12 + 1)
            v10 += v3[v12]
            v9[v12] = 0
        if v11 + sum((v9[v12] * 100 * (v12 + 1) for v12 in range(v1))) < v2:
            continue
    v13 = v1 - 1
    while v11 < v2:
        while not v9[v13]:
            v13 -= 1
        v11 += 100 * (v13 + 1)
        v9[v13] -= 1
        v10 += 1
    if v10 < v7:
        v7 = v10
print(v7)

v1, v2 = map(int, input().split())
v3 = []
v4 = 0
for v5 in range(1, v1 + 1):
    v6, v7 = map(int, input().split())
    v4 += v6
    for v8 in range(1, v6 + 1):
        v3 += [(v8, v5 * 100 * v8 + v7 * (v8 == v6))]
v9 = [0] * (v4 + 1)
for v10, v11 in v3:
    if v10 == 1:
        v12 = v9[:]
    for v13 in range(1, v4 + 1):
        if v13 >= v10:
            v9[v13] = max(v9[v13], v12[v13 - v10] + v11)
for v5 in range(v4 + 1):
    if v9[v5] >= v2:
        print(v5)
        break

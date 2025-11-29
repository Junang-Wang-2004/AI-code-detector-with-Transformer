v1, v2, v3 = map(int, input().split())
v4 = [[0 for v5 in range(v2)] for v5 in range(v1)]
v6 = []
v7 = []
v8 = 0
for v9 in range(v1):
    v10 = list(input())
    if '#' not in v10:
        v6.append(v9)
        continue
    v7.append(v9)
    v11 = 0
    v8 += 1
    for v12 in range(v2):
        if v10[v12] == '#':
            if not v11:
                v11 = 1
            else:
                v8 += 1
        v4[v9][v12] = v8
for v9 in v6:
    v13 = v9
    v11 = 0
    while v13 in v6:
        if v13 == v1 - 1:
            v11 = 1
        if v11:
            v13 -= 1
        else:
            v13 += 1
    v4[v9] = v4[v13].copy()
for v14 in v4:
    print(*v14)

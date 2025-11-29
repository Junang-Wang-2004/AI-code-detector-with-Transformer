import copy
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6, v7 = map(int, input().split())
    v3.append([v5, v6, v7])
v8 = 0
for v4 in range(2 ** 3):
    v9 = [[0] * (v2 + 1) for v10 in range(v1 + 1)]
    v11 = copy.deepcopy(v3)
    for v12 in range(3):
        if v4 >> v12 & 1:
            for v13 in range(v1):
                v11[v13][v12] *= -1
    for v14 in range(1, v1 + 1):
        for v15 in range(1, v2 + 1):
            if v15 <= v14:
                v9[v14][v15] = max([v9[v14 - 1][v15], v9[v14 - 1][v15 - 1] + sum(v11[v14 - 1]), v9[v14][v15]])
            else:
                v9[v14][v15] = max([v9[v14 - 1][v15], v9[v14][v15]])
    v8 = max(v8, v9[v1][v2])
print(v8)

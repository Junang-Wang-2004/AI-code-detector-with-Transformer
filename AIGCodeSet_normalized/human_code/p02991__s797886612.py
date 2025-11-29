v1, v2 = map(int, input().split())
v3 = [[False, False, False] for v4 in range(v1)]
v5 = [[] for v4 in range(v1)]
for v6 in range(v2):
    v7, v8 = map(int, input().split())
    v5[v7 - 1].append(v8)
v9, v10 = map(int, input().split())
v11 = [(v9, 0)]
v3[v9 - 1][2] = True
v12 = -1
while len(v11) > 0:
    v13, v14 = v11.pop(0)
    if v13 == v10:
        v12 = v14
        break
    for v6 in v5[v13 - 1]:
        if not v3[v6 - 1][0]:
            v3[v6 - 1][0] = True
            for v15 in v5[v6 - 1]:
                if not v3[v15 - 1][1]:
                    v3[v15 - 1][1] = True
                    for v16 in v5[v15 - 1]:
                        if not v3[v16 - 1][2]:
                            v3[v16 - 1][2] = True
                            v11.append((v16, v14 + 1))
print(v12)

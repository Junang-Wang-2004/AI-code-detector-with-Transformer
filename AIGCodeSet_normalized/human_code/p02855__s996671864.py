v1, v2, v3 = map(int, input().split())
v4 = [input() for v5 in range(v1)]
v6 = []
v7 = 0
v8 = 0
for v9 in range(v1):
    if v4[v9] == '.' * v2:
        v7 += 1
        continue
    else:
        v8 += 1
        v10 = []
        v11 = False
        for v12 in range(v2):
            if v4[v9][v12] == '#':
                if not v11:
                    v11 = True
                else:
                    v8 += 1
            v10.append(v8)
        for v5 in range(v7 + 1):
            v6.append(v10)
        v7 = 0
for v5 in range(v7):
    v6.append(v6[-1])
for v13 in v6:
    print(*v13, sep=' ')

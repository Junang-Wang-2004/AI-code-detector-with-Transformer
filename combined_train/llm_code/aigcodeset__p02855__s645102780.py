v1, v2, v3 = map(int, input().split())
v4 = tuple((tuple(input()) for v5 in range(v1)))
v6 = [[0 for v5 in range(v2)] for v7 in range(v1)]
v8 = 1
v9 = []
for v5 in range(v1):
    if '#' in v4[v5]:
        v10 = v4[v5].index('#')
        for v7 in range(v10 + 1):
            v6[v5][v7] = v8
        for v7 in range(v10 + 1, v2):
            if v4[v5][v7] == '#':
                v8 += 1
            v6[v5][v7] = v8
        v8 += 1
    else:
        v9.append(v5)
v11 = tuple(set(range(v1)) - set(v9))
for v5 in range(v11[0]):
    v6[v5] = v6[v11[0]]
v12 = 0
for v5 in range(v11[0] + 1, v1):
    if v5 in v11:
        v12 += 1
        continue
    else:
        v6[v5] = v6[v12]
for v5 in v6:
    print(' '.join(map(str, v5)))

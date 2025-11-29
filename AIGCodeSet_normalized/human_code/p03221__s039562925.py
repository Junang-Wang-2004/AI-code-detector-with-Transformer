v1, v2 = map(int, input().split())
v3 = [tuple(map(int, input().split())) for v4 in range(v2)]
v5 = [list() for v4 in range(v1)]
v6 = [dict() for v4 in range(v1)]
for v7 in v3:
    v5[v7[0] - 1].append(v7[1])
for v8 in range(v1):
    v5[v8].sort()
    v6[v8] = dict(zip(v5[v8], range(1, len(v5[v8]) + 1)))
for v7 in v3:
    v9 = v7[0]
    v10 = v6[v7[0] - 1][v7[1]]
    print('{:06}{:06}'.format(v9, v10))

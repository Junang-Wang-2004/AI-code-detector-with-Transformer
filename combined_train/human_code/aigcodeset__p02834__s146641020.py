v1, v2, v3 = map(int, input().split())
v4 = [set() for v5 in range(v1 + 1)]
for v5 in range(v1 - 1):
    v6, v7 = map(int, input().split())
    v4[v6].add(v7)
    v4[v7].add(v6)
v8 = [v3]
v9 = []
v10 = set([v3])
v11 = [set() for v5 in range(v1 + 1)]
v12 = [0] * (v1 + 1)
while v8:
    v13 = v8.pop()
    if v13 > 0:
        v9.append(v13)
        if v13 == v2:
            v14 = len(v9) // 2
            v15 = v9[-v14]
        for v16 in v4[v13]:
            if v16 in v10:
                continue
            v12[v16] = v12[v13] + 1
            v11[v13].add(v16)
            v10.add(v16)
            v8 += [-v13, v16]
    else:
        v9.pop()
v8 = [v15]
v10 = set([v15])
while v8:
    v13 = v8.pop()
    for v16 in v11[v13]:
        if v16 in v10:
            continue
        v10.add(v16)
        v8.append(v16)
v17 = 0
for v13 in v10:
    v17 = max(v12[v13], v17)
print(v17 - 1)

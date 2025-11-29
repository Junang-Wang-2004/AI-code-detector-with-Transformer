v1, v2, v3 = map(int, input().split())
v4 = 0
v2 -= 1
v3 -= 1
v5 = [[] for v6 in range(v1)]
v7 = float('inf')
v8 = [v7] * v1
for v9 in range(v1 - 1):
    v10, v11 = map(int, input().split())
    v10 -= 1
    v11 -= 1
    v5[v10].append(v11)
    v5[v11].append(v10)
v12 = v5[v3]
v8[v3] = 0
v13 = 1
v14 = {v3}
while v12:
    v15 = []
    for v9 in v12:
        v14.add(v9)
        for v16 in v5[v9]:
            if v16 not in v14:
                v15.append(v16)
        v8[v9] = v13
    v13 += 1
    v12 = v15
v12 = v5[v2]
v17 = [-1] * v1
v17[v2] = 0
v13 = 1
v14 = {v2}
v18 = -1
while v12:
    v15 = []
    for v9 in v12:
        v14.add(v9)
        for v16 in v5[v9]:
            if v8[v16] <= v13 + 1:
                if v8[v16] == v13 + 1:
                    v4 = 1
                if v18 < 0:
                    v18 = v9
                continue
            if v16 not in v14:
                v15.append(v16)
        v17[v9] = v13
    v13 += 1
    v12 = v15
v12 = v5[v18]
v13 = v17[v18] + 1
v14 = {v18}
while v12:
    v15 = []
    for v9 in v12:
        v14.add(v9)
        if v17[v9] == -1:
            continue
        v17[v9] = max(v13, v17[v9])
        for v16 in v5[v9]:
            if v16 not in v14:
                v15.append(v16)
    v13 += 1
    v12 = v15
v19 = 0
for v9 in range(v1):
    if v8[v9] > v17[v9]:
        v19 = max(v19, v17[v9])
print(v19 + v4)

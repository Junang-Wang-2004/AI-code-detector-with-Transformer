v1 = input()
v2, v3 = map(int, input().split())
v4 = 0
v5 = []
v6 = 0
v7 = len(v1)
v8 = []
for v9 in range(len(v1)):
    v10 = v1[v9]
    if v10 == 'F':
        v4 += 1
    else:
        v7 = v9 + 0
        break
v11 = 0
v12 = 0
for v9 in range(v7, len(v1)):
    v10 = v1[v9]
    if v10 == 'F':
        if v6 % 2 == 0:
            v11 += 1
        else:
            v12 += 1
    elif v6 % 2 == 0:
        if v11 != 0:
            v8.append(v11)
        v11 = 0
        v6 += 1
    else:
        if v12 != 0:
            v5.append(v12)
        v12 = 0
        v6 += 1
if v11 != 0:
    v8.append(v11)
if v12 != 0:
    v5.append(v12)
v13 = set([v4])
for v9 in v8:
    v14 = len(v13)
    v15 = list(v13)
    v13 = set([])
    for v16 in range(v14):
        v13.add(v15[v16] + v9)
        v13.add(v15[v16] - v9)
v17 = set([0])
for v9 in v5:
    v14 = len(v17)
    v18 = list(v17)
    v17 = set([])
    for v16 in range(v14):
        v17.add(v18[v16] + v9)
        v17.add(v18[v16] - v9)
if v2 in v13 and v3 in v17:
    print('Yes')
else:
    print('No')

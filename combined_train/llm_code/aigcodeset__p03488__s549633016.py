v1 = input()
v2, v3 = map(int, input().split())
v4 = []
v5 = []
v6 = 15000
v7 = [False for v8 in range(v6 * 2 + 1)]
v9 = [False for v8 in range(v6 * 2 + 1)]
v7[v6] = True
v9[v6] = True
v10 = True
v11 = 0
for v12 in v1:
    if v12 == 'T':
        if v10:
            v4.append(v11)
            v11 = 0
            v10 = False
        else:
            v5.append(v11)
            v11 = 0
            v10 = True
    else:
        v11 += 1
if v10:
    v4.append(v11)
    v11 = 0
    v10 = False
else:
    v5.append(v11)
    v11 = 0
    v10 = True
for v13 in v4:
    v14 = []
    for v8 in range(len(v7)):
        if v7[v8]:
            if v8 + v13 <= v6 * 2:
                v14.append(v8 + v13)
            if v8 - v13 >= 0:
                v14.append(v8 - v13)
            v7[v8] = False
    for v15 in v14:
        v7[v15] = True
for v13 in v5:
    v14 = []
    for v8 in range(len(v9)):
        if v9[v8]:
            if v8 + v13 <= v6 * 2:
                v14.append(v8 + v13)
            if v8 - v13 >= 0:
                v14.append(v8 - v13)
            v9[v8] = False
    for v15 in v14:
        v9[v15] = True
if v7[v2 + v6] and v9[v3 + v6]:
    print('Yes')
else:
    print('No')

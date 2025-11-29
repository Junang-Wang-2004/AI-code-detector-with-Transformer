v1 = int(input())
v2 = [input() for v3 in range(v1)]
v4 = [[0] * 2 for v3 in range(v1)]
for v5 in range(v1):
    v6 = v2[v5]
    v7 = 0
    v8 = 0
    v9 = 0
    for v10 in v6:
        if v10 == ')':
            v9 += 1
        else:
            v8 += 1
        v7 = max(v7, v9 - v8)
    v4[v5] = [v8 - v9, v7, v6]
v11 = 0
v12 = []
v13 = []
for v14, v15, v6 in v4:
    if v14 >= 0:
        if v15 <= 0:
            v11 += v14
        else:
            v12.append([v14, v15])
    else:
        v13.append([v14, v15, v6])
v12.sort(key=lambda x: v14[1])
for v14, v15 in v12:
    if v15 > v11:
        print('No')
        exit()
    v11 += v14
if len(v13) == 0:
    if v11 == 0:
        print('Yes')
    else:
        print('No')
    exit()
v13.sort(reverse=True)
v13.sort(key=lambda x: v14[1], reverse=True)
for v5 in range(len(v13)):
    v14, v15, v6 = v13[v5]
    if v14 == -v15:
        v16 = v14
        v13[v5] = [0, 0, '']
        break
else:
    print('No')
    exit()
for v14, v15, v6 in v13:
    if v11 < v15:
        print('No')
        exit()
    v11 += v14
if v11 + v16 == 0:
    print('Yes')
else:
    print('No')

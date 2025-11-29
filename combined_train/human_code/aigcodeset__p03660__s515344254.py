v1, *v2 = map(int, open(0).read().split())
v3 = [[] for v4 in range(v1)]
v5 = [-1] * v1
v5[0] = 0
v6 = [-1] * v1
v6[-1] = 0
for v7, v8 in zip(*[iter(v2)] * 2):
    v3[v7 - 1] += [v8 - 1]
    v3[v8 - 1] += [v7 - 1]
v9 = [0]
while v9:
    v10 = v9.pop(0)
    for v11 in v3[v10]:
        if v5[v11] < 0:
            v9.append(v11)
            v5[v11] = v5[v10] + 1
v9 = [v1 - 1]
while v9:
    v10 = v9.pop(0)
    for v11 in v3[v10]:
        if v6[v11] < 0:
            v9.append(v11)
            v6[v11] = v6[v10] + 1
v8 = v12 = 0
for v13, v14 in zip(v5, v6):
    if v13 <= v14:
        v8 += 1
    else:
        v12 += 1
if v8 <= v12:
    print('Snuke')
else:
    print('Fennec')

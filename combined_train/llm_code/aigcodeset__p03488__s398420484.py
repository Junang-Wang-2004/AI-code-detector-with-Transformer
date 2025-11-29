v1 = input().strip()
v2, v3 = map(int, input().split())
v4 = []
v5 = []
v6 = 0
v7 = 0
for v8 in range(len(v1)):
    if v1[v8] == 'F':
        v7 += 1
    elif v6 == 0:
        if v7 > 0:
            v4.append(v7)
            v7 = 0
        v6 = 1
    else:
        if v7 > 0:
            v5.append(v7)
            v7 = 0
        v6 = 0
if v7 > 0 and v6 == 0:
    v4.append(v7)
if v7 > 0 and v6 == 1:
    v5.append(v7)
v9 = sum(v4)
v10 = [[0 for v11 in range(2 * v9 + 1)] for v11 in range(len(v4) + 1)]
if v1[0] == 'F':
    v10[0][v9] = 1
    v10[1][v9 + v4[0]] = 1
    for v8 in range(1, len(v4)):
        for v12 in range(2 * v9 + 1):
            if v12 + v4[v8] <= 2 * v9:
                v10[v8 + 1][v12 + v4[v8]] = v10[v8 + 1][v12 + v4[v8]] or v10[v8][v12]
            if 0 <= v12 - v4[v8]:
                v10[v8 + 1][v12 - v4[v8]] = v10[v8 + 1][v12 - v4[v8]] or v10[v8][v12]
else:
    v10[0][v9] = 1
    for v8 in range(len(v4)):
        for v12 in range(2 * v9 + 1):
            if v12 + v4[v8] <= 2 * v9:
                v10[v8 + 1][v12 + v4[v8]] = v10[v8 + 1][v12 + v4[v8]] or v10[v8][v12]
            if 0 <= v12 - v4[v8]:
                v10[v8 + 1][v12 - v4[v8]] = v10[v8 + 1][v12 - v4[v8]] or v10[v8][v12]
v13 = sum(v5)
v14 = [[0 for v11 in range(2 * v13 + 1)] for v11 in range(len(v5) + 1)]
v14[0][v13] = 1
for v8 in range(len(v5)):
    for v12 in range(2 * v13 + 1):
        if v12 + v5[v8] <= 2 * v13:
            v14[v8 + 1][v12 + v5[v8]] = v14[v8 + 1][v12 + v5[v8]] or v14[v8][v12]
        if 0 <= v12 - v5[v8]:
            v14[v8 + 1][v12 - v5[v8]] = v14[v8 + 1][v12 - v5[v8]] or v14[v8][v12]
if v9 == 0 and v2 != 0 or (v13 == 0 and v3 != 0):
    print('No')
elif v10[len(v4)][v9 + v2] == 1 and v14[len(v5)][v13 + v3] == 1:
    print('Yes')
else:
    print('No')

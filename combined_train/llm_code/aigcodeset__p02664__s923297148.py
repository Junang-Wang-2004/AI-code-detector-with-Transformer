v1 = list(input())
v2 = 0
v3 = []
v4 = 0
v5 = len(v1)
for v6 in range(v5):
    if v1[v6] == '?':
        v2 += 1
v7 = 2 ** v2
v8 = [[''] * v5 for v6 in range(v7)]
for v6 in range(v5):
    if v1[v6] != '?':
        for v9 in range(v7):
            v8[v9][v6] = v1[v6]
    else:
        for v9 in range(v7):
            if v9 % 2 == 0:
                v8[v9][v6] = 'P'
            else:
                v8[v9][v6] = 'D'
for v10 in range(v7):
    v11 = 0
    for v6 in range(v5 - 1):
        if v8[v10][v6] == 'P' and v8[v10][v6 + 1] == 'D':
            v11 += 1
        elif v8[v10][v6 + 1] == 'D':
            v11 += 1
    v3.append(v11)
for v6 in range(v7):
    if v3[v6] > v3[v4]:
        v4 = v6
print(''.join(v8[v4]))

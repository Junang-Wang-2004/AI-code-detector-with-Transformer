import sys
input = sys.stdin.readline
v1 = list(input().strip())
v2, v3 = map(int, input().split())
v3 = abs(v3)
v1.append('T')
v4 = []
v5 = []
v6 = 0
v7 = 0
for v8 in range(len(v1)):
    if v1[v8] == 'F':
        v6 += 1
    elif v7 % 2 == 0:
        v4.append(v6)
        v7 += 1
        v6 = 0
    else:
        v5.append(v6)
        v7 += 1
        v6 = 0
v9 = sum(v4)
v10 = sum(v5)
if v9 < v2 or v10 < v3:
    print('No')
    exit()
v11 = [[0 for v8 in range(v9 + 1)] for v12 in range(len(v4) + 1)]
v11[0][v9] = 1
v2 -= v4[0]
v4[0] = 0
v9 -= v4[0]
v2 = abs(v2)
for v8 in range(len(v4)):
    for v12 in range(v9 + 1):
        if v11[v8][v12] == 1:
            if v12 - 2 * v4[v8] >= 0:
                v11[v8 + 1][v12 - 2 * v4[v8]] = 1
            v11[v8 + 1][v12] = 1
if len(v5) == 0:
    v5.append(0)
v13 = [[0 for v8 in range(v10 + 1)] for v12 in range(len(v5) + 1)]
v13[0][v10] = 1
for v8 in range(len(v5)):
    for v12 in range(v10 + 1):
        if v13[v8][v12] == 1:
            if v12 - 2 * v5[v8] >= 0:
                v13[v8 + 1][v12 - 2 * v5[v8]] = 1
            v13[v8 + 1][v12] = 1
if v13[-1][v3] == 1 and v11[-1][v2] == 1:
    print('Yes')
else:
    print('No')

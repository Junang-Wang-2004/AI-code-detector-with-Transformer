v1, v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v1):
    v7 = list(map(int, input().split()))
    v4.append(v7[0])
    v5.append(v7[1:])
v8 = 10 ** 10
for v6 in range(2 ** v1):
    v9 = [0 for v10 in range(v2)]
    v11 = '{:b}'.format(v6)
    v12 = v11.zfill(v1)
    v13 = 0
    for v14 in range(len(v12)):
        if v12[v14] == '1':
            for v15 in range(v2):
                v9[v15] += v5[v14][v15]
            v13 += v4[v14]
    if all((u >= v3 for v16 in v9)):
        v8 = min(v8, v13)
if v8 == 10 ** 10:
    print(-1)
else:
    print(v8)

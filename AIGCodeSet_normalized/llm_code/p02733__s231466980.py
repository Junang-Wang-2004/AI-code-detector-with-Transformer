v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v4.append(list(map(int, input())))
v6 = 0
for v7 in range(2 ** (v1 - 1)):
    v8 = 0
    v9 = []
    v9.append(v4[0])
    for v10 in range(v1 - 1):
        if v7 >> v10 & 1:
            v8 += 1
            v9.append(v4[v10 + 1])
        else:
            v9[v8] = [v9[v8][j] + v4[v10 + 1][j] for v11 in range(v2)]
    v12 = True
    v13 = 0
    v14 = 0
    for v15 in range(1, v2 + 1):
        v16 = True
        for v17 in v9:
            if sum(v17[v14:v15]) > v3:
                v16 = False
                break
        if v16:
            v18 = v15
        elif v18 != v14:
            v14 = v18
            v13 += 1
        else:
            v12 = False
            break
    if v12:
        v19 = bin(v7).count('1') + v13
        v6 = v19 if v6 > v19 else v6
print(v6)

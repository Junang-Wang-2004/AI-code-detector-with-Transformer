v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v6 = list(map(int, input().split()))
    v7 = [v6[0], v6[1:]]
    v4.append(v7)
for v8 in range(1, 2 ** v1):
    v7 = [1 if v8 >> v5 & 1 else 0 for v5 in range(v1)]
    v9 = -1
    for v8 in range(2 ** v1):
        v10 = v7[v8]
        v11 = [0 for v5 in range(v1)]
        v12 = 0
        for v5 in range(v1):
            v13 = v10[v5]
            v13 = int(v13)
            if v13 == 1:
                for v14 in range(v2):
                    v11[v14] += v4[v5][1][v14]
                v12 += v4[v5][0]
        v15 = 1
        for v5 in range(v2):
            if v11[v5] < v3:
                v15 = 0
        if v15 == 1:
            if v9 == -1:
                v9 = v12
            else:
                v9 = min(v9, v12)
    print(v9)

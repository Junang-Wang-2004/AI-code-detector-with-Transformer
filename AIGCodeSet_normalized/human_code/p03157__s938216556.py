v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v3.append(input())

def f1(a1, a2):
    v1 = []
    for v2 in [1, -1]:
        if 0 <= a1 + v2 < v1:
            if v3[a1][a2] != v3[a1 + v2][a2]:
                v1.append((a1 + v2, a2))
        if 0 <= a2 + v2 < v2:
            if v3[a1][a2] != v3[a1][a2 + v2]:
                v1.append((a1, a2 + v2))
    return v1
v5 = [[0 for v6 in range(v2)] for v7 in range(v1)]
v8 = 0
for v6 in range(v1):
    for v7 in range(v2):
        if v5[v6][v7] == 0:
            v5[v6][v7] = 1
            v9 = 0
            v10 = 0
            if v3[v6][v7] == '#':
                v9 += 1
            else:
                v10 += 1
            v11 = f1(v6, v7)
            while len(v11) > 0:
                v12 = []
                for v13 in v11:
                    v14, v15 = v13
                    if v5[v14][v15] == 0:
                        v5[v14][v15] = 1
                        if v3[v14][v15] == '#':
                            v9 += 1
                        else:
                            v10 += 1
                        for v16 in f1(v14, v15):
                            if v5[v16[0]][v16[1]] == 0:
                                v12.append(v16)
                v11 = v12
            v8 += v9 * v10
print(v8)

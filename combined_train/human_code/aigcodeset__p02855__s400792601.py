def f1(a1, a2, a3, a4):
    v1 = a2 - 1
    if v1 < 0:
        return
    elif a1[v1][a3] != 0:
        return
    else:
        a1[v1][a3] = a4
        f1(a1, v1, a3, a4)

def f2(a1, a2, a3, a4):
    v1 = a2 + 1
    if v1 >= len(a1):
        return
    elif a1[v1][a3] != 0:
        return
    else:
        a1[v1][a3] = a4
        f2(a1, v1, a3, a4)
v1, v2, v3 = map(int, input().split())
v4 = []
for v5 in range(v1):
    v6 = input()
    v7 = []
    for v8 in range(len(v6)):
        if v6[v8] == '#':
            v7.append(1)
        else:
            v7.append(0)
    v4.append(v7)
v9 = [[0] * v2 for v5 in range(v1)]
v10 = 1
for v5 in range(v1):
    v11 = v4[v5].count(1)
    if v11 == 0:
        continue
    else:
        v12 = True
        for v8 in range(v2):
            if v4[v5][v8] == 0:
                v9[v5][v8] = v10
            elif v12:
                v9[v5][v8] = v10
                v12 = False
            else:
                v10 += 1
                v9[v5][v8] = v10
        v10 += 1
for v5 in range(v1):
    for v8 in range(v2):
        if v9[v5][v8] != 0:
            f1(v9, v5, v8, v9[v5][v8])
            f2(v9, v5, v8, v9[v5][v8])
for v5 in range(v1):
    print(' '.join(list(map(str, v9[v5]))))

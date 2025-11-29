def f1():
    v1, v2 = IL()
    v3 = ILL(v1)
    v4 = 0
    v5 = -1
    v6 = None
    if v1 % 2 == 1:
        v7 = v2 - 1
    else:
        v7 = 0
    v8 = v1 - 1
    v9 = []
    while v4 != v7 or v5 != v8:
        if v4 == 0:
            if v5 % 2 == 1:
                v5 += 1
            else:
                v4 += 1
        elif v4 == v2 - 1:
            if v5 % 2 == 1:
                v4 -= 1
            else:
                v5 += 1
        elif v5 % 2 == 1:
            v4 -= 1
        else:
            v4 += 1
        if v6 == None:
            if v3[v5][v4] % 2 == 1:
                v6 = (v5, v4)
        elif v3[v5][v4] % 2 == 1:
            v9.append([v6[0] + 1, v6[1] + 1, v5 + 1, v4 + 1])
            v6 = None
        else:
            v9.append([v6[0] + 1, v6[1] + 1, v5 + 1, v4 + 1])
            v6 = (v5, v4)
    print(len(v9))
    for v10 in v9:
        print(*v10)

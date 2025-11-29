def f1(a1):
    v1 = 0
    v2 = 1
    while v2 != len(a1):
        v3 = a1[v2]
        v4 = -1
        v5 = None
        for v6 in v3:
            if v6[1] > v4:
                v4 = v6[1]
                v5 = v6[0]
        v2 = v5
        v1 += v4
    return v1

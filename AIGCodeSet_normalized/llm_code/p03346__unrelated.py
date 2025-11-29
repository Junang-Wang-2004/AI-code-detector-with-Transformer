def f1(a1):
    v1 = len(a1)
    v2 = 0
    for v3 in range(v1):
        for v4 in range(v3 + 1, v1):
            if a1[v3] > a1[v4]:
                a1[v3], a1[v4] = (a1[v4], a1[v3])
                v2 += 1
    return v2

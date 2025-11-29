def f1(a1):
    v1 = len(a1)
    v2 = v1 // 2
    for v3 in range(v2, 0, -1):
        if a1[:v3] == a1[v3:2 * v3]:
            return 2 * v3
    return 0

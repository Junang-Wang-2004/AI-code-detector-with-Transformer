def f1(a1, a2):
    v1 = 0
    for v2 in range(a1):
        for v3 in range(a1):
            if abs(a2[v2] - a2[v3]) <= 1:
                v1 += 1
    return v1

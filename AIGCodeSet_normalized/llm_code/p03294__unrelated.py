def f1(a1):
    v1 = 0
    for v2 in range(1, 10000):
        v3 = 0
        for v4 in a1:
            v3 += v2 % v4
        if v3 > v1:
            v1 = v3
    return v1

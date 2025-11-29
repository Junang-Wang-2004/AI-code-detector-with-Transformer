def f1(a1, a2):
    v1 = 0
    for v2 in range(1, a1 + 1):
        if len(str(v2)) == a2:
            v1 += 1
    return v1

def f1(a1, a2):
    v1 = 0
    for v2 in range(len(a1)):
        if a1[v2] == a2[v2]:
            v1 += 1
    return v1

def f1(a1):
    v1 = 0
    for v2 in range(len(a1)):
        if a1[v2] == '#' and v2 < len(a1) - 1 and (a1[v2 + 1] == '.'):
            v1 += 1
    return v1

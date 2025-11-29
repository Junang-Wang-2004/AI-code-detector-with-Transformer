def f1(a1):
    v1 = 10 ** 9 + 7
    a1 = bin(a1)[2:]
    v3 = len(a1)
    v4 = 1
    for v5 in range(v3):
        v4 = v4 * 2 % v1
    return v4 - 1

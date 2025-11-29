def f1(a1, a2, a3):
    v1 = 10 ** 9 + 7
    v2 = [0] * (a2 + 1)
    v2[0] = 1
    for v3 in a3:
        for v4 in range(a2, v3 - 1, -1):
            v2[v4] = (v2[v4] + v2[v4 - v3]) % v1
    return v2[a2]

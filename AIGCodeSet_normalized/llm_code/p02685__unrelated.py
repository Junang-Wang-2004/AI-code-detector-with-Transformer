def f1(a1, a2, a3):
    v1 = [1] * (a1 + 1)
    for v2 in range(1, a1 + 1):
        for v3 in range(1, a2 + 1):
            if v2 > 1 and v1[v2 - 1] != v3:
                v1[v2] += v1[v2 - 1]
            if v2 < a1 and v1[v2 + 1] != v3:
                v1[v2] += v1[v2 + 1]
    return v1[a1] % 998244353

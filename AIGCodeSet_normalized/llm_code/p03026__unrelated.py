def f1(a1, a2, a3, a4):
    v1 = 0
    for v2 in range(1, a1 + 1):
        if len(a2[v2]) == 0:
            v1 += a4[v2]
            continue
        v3 = min((a4[u] for v4 in a2[v2]))
        v1 += v3
    return v1

def f1(a1, a2, a3, a4):
    v1 = 0
    v2 = set()
    a4.sort(reverse=True)
    for v3 in range(a1):
        if a4[v3] not in v2 and a2 <= a4[v3] <= a3:
            v2.add(a4[v3])
            for v4 in range(v3 + 1, a1):
                if a4[v4] not in v2 and a2 < a4[v4] <= a3:
                    for v5 in range(v4 + 1, a1):
                        if a4[v5] not in v2 and a3 < a4[v5]:
                            v1 += 1
                            v2.add(a4[v4])
                            v2.add(a4[v5])
                            break
    return v1

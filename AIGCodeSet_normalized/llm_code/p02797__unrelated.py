def f1(a1, a2, a3):
    v1 = [1]
    while len(v1) < a1:
        v2 = sum(v1)
        if v2 == a3:
            return v1
        for v3 in range(1, 10):
            if v3 not in v1:
                v1.append(v3)
                break
    return []

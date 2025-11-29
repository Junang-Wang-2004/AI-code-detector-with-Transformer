def f1(a1):
    v1 = []
    for v2 in range(1, len(a1) + 1):
        v1.append(v2)
        if v1 != a1:
            return False
    return True

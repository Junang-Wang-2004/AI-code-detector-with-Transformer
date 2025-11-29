def f1():
    v1 = int(input())
    v2 = 0
    for v3 in range(1, v1 + 1, 2):
        v4 = factorize(v3)
        v5 = []
        for v6 in v4:
            v5.append(v6)
            if v3 // v6 != v6:
                v5.append(v3 // v6)
        v5.append(v3)
        v5.append(1)
        v7 = len(set(v5))
        if v7 == 8:
            v2 += 1
    return v2
print(f1())

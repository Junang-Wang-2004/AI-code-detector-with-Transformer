def f1(a1):
    v1 = []
    v2 = 0
    v3 = len(a1)
    while v2 < v3:
        v1.append(a1[v2])
        v4 = v2 + 1
        while v4 < v3 and sorted(a1[v4]) == sorted(a1[v2]):
            v4 += 1
        v2 = v4
    return v1

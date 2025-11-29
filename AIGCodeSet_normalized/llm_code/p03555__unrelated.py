def f1(a1):
    v1 = a1.splitlines()
    if len(v1) != 2 or len(v1[0]) != 3:
        return 'NO'
    for v2 in range(2):
        for v3 in range(3):
            if v1[v2][v3] != v1[1 - v2][2 - v3]:
                return 'NO'
    return 'YES'

v1 = 10 ** 9 + 7

def f1():
    v1, v2 = [int(s) for v3 in input().split()]
    print(f2(v2, v1))

def f2(a1, a2):
    v1 = list(f3(a1))
    v2 = max((c for v3, v4 in v1))
    v5 = dict()
    v5[1] = [1 for v6 in range(v2 + 1)]
    v7 = 1
    while v7 < a2:
        v8 = v7 - 1
        v5[v7 * 2] = [0 for v6 in range(v2 + 1)]
        if v8 != 0:
            v5[v7 + v8] = [0 for v6 in range(v2 + 1)]
        for v9 in range(v2 + 1):
            for v10 in range(v2 + 1 - v9):
                v5[v7 * 2][v9 + v10] = (v5[v7 * 2][v9 + v10] + v5[v7][v9] * v5[v7][v10]) % v1
                if v8 != 0:
                    v5[v7 + v8][v9 + v10] = (v5[v7 + v8][v9 + v10] + v5[v7][v9] * v5[v8][v10]) % v1
        v7 *= 2
    v11 = 1
    for v3, v4 in v1:
        v11 = v11 * v5[a2][v4] % v1
    return v11

def f3(a1):
    import itertools
    v1 = a1
    for v2 in itertools.count(2):
        if v2 * v2 > v1:
            break
        v3 = 0
        while True:
            v4, v5 = divmod(v1, v2)
            if v5 != 0:
                break
            v3 += 1
            v1 = v4
        if v3 != 0:
            yield (v2, v3)
    if v1 != 1:
        yield (v1, 1)
f1()

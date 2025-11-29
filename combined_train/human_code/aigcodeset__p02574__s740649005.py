def f1():
    from math import gcd
    import sys
    input = sys.stdin.buffer.readline
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = v2[0]
    for v4 in v2:
        v3 = gcd(v3, v4)
    if v3 != 1:
        print('not coprime')
        exit()
    v5 = 10 ** 3 + 1
    v6 = [True for v7 in range(v5)]
    v6[0] = v6[1] = False
    v8 = []
    for v9 in range(2, int(v5 ** 0.5 + 1)):
        if not v6[v9]:
            continue
        v8.append(v9)
        for v10 in range(v9 * 2, v5, v9):
            v6[v10] = False
    v11 = [False for v7 in range(v5)]
    for v9 in range(v1):
        for v12 in v8:
            if v2[v9] % v12 == 0:
                if v11[v12]:
                    print('setwise coprime')
                    exit()
                while v2[v9] % v12 == 0:
                    v2[v9] //= v12
                    v11[v12] = True
    v2.sort()
    v13 = 1
    for v4 in v2:
        if v4 == 1:
            continue
        elif v4 == v13:
            print('setwise coprime')
            exit()
        v13 = v4
    print('pairwise coprime')
f1()

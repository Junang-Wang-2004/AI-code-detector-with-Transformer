import sys

def f1(a1, a2, a3, a4, a5):
    v1 = []
    for v2 in range(a2):
        v3 = 0
        for v4 in range(a4[v2]):
            v3 |= 1 << a5[v2][v4] - 1
        v1.append([v3, a3[v2]])
    v5 = 1001001001
    v6 = [v5] * (1 << a1)
    v6[0] = 0
    for v3 in range(1 << a1):
        for v2 in range(a2):
            v7 = v3 | v1[v2][0]
            v8 = v6[v3] + v1[v2][1]
            v6[v7] = min(v6[v7], v8)
    v9 = v6[-1]
    print(-1 if v9 == v5 else v9)
    pass

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4, v5, v6 = ([], [], [])
    for v7 in range(v3):
        v4.append(int(next(v1)))
        v5.append(int(next(v1)))
        v6.append([int(next(v1)) for v7 in range(v5[-1])])
    f1(v2, v3, v4, v5, v6)
if __name__ == '__main__':
    f2()

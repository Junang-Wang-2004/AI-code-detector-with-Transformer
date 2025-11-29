import sys

def f1(a1: int, a2: 'List[int]'):
    for v1 in range(a1 + 1):
        if a2[v1] > 2 ** v1:
            print(-1)
            return
        elif a2[v1] == 2 ** v1 and v1 != a1:
            print(-1)
            return
        else:
            continue
    if a1 == 0:
        print(1)
        return
    v2 = [0] * (a1 + 1)
    v2[a1] = a2[a1]
    for v1 in range(a1 - 1, -1, -1):
        v2[v1] = v2[v1 + 1] + a2[v1]
    v3 = [0] * (a1 + 1)
    v3[0] = 1
    v4 = 1
    for v1 in range(1, a1 + 1):
        if v3[v1 - 1] * 2 > v2[v1]:
            v3[v1] = v2[v1]
            v4 += v3[v1]
            v3[v1] -= a2[v1]
        else:
            v3[v1] = v3[v1 - 1] * 2
            v4 += v3[v1]
            v3[v1] -= a2[v1]
    print(v4)
    return

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = [int(next(v1)) for v4 in range(v2 - 0 + 1)]
    f1(v2, v3)
if __name__ == '__main__':
    f2()

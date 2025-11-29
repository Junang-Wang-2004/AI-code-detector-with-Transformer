import sys
from itertools import combinations

def f1(a1, a2):
    if a2 == 0:
        yield []
        return
    if a2 == 1:
        yield [a1]
        return
    for v1 in range(a1 + 1):
        for v2 in f1(a1 - v1, a2 - 1):
            yield ([v1] + v2)

def f2(a1: int, a2: int, a3: int, a4: 'List[int]', a5: 'List[int]', a6: 'List[int]', a7: 'List[int]'):
    v1 = 0
    for v2 in range(a2):
        for v3 in f1(v2, a1 - 1):
            v4 = 0
            v5 = [1] * a1
            for v6, v7 in enumerate(v3):
                v5[v6 + 1] = v5[v6] + v7
            for v8 in range(a3):
                if v5[a5[v8] - 1] - v5[a4[v8] - 1] == a6[v8]:
                    v4 += a7[v8]
            v1 = max(v1, v4)
    print(v1)
    return

def f3():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4 = int(next(v1))
    v5 = [int()] * v4
    v6 = [int()] * v4
    v7 = [int()] * v4
    v8 = [int()] * v4
    for v9 in range(v4):
        v5[v9] = int(next(v1))
        v6[v9] = int(next(v1))
        v7[v9] = int(next(v1))
        v8[v9] = int(next(v1))
    f2(v2, v3, v4, v5, v6, v7, v8)
if __name__ == '__main__':
    f3()

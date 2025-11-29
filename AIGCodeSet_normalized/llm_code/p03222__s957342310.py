from itertools import product
import sys
try:
    from typing import Dict, List, Tuple
except ImportError:
    pass
v1 = 1000000007

def f1(a1: 'Tuple[bool]'):
    return not any((h1 and h2 for v1, v2 in zip(a1, a1[1:])))

def f2(a1: int, a2: int, a3: int):
    v1: 'List[Tuple[bool]]' = [ptn for v2 in product((False, True), repeat=a2 - 1) if f1(v2)]
    v3: 'List[int]' = [1 if i == a3 - 1 else 0 for v4 in range(a2)]
    for v5 in range(a1):
        v6: 'List[int]' = [0] * a2
        for v2 in v1:
            for v7 in range(a2):
                v8 = v7
                if v7 < a2 - 1 and v2[v7]:
                    v8 = v7 + 1
                elif v7 > 0 and v2[v7 - 1]:
                    v8 = v7 - 1
                v6[v8] += v3[v7]
                v6[v8] %= v1
        v3 = v6
    print(v3[a3 - 1])

def f3():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4 = int(next(v1))
    f2(v2, v3, v4)
if __name__ == '__main__':
    f3()

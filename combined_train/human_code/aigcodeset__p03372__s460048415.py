import sys
from collections.abc import Iterable
from math import *
from itertools import *
from collections import *
from functools import *
from operator import *
try:
    from math import gcd
except Exception:
    from fractions import gcd

def f1(a1: int, a2: int, a3: 'List[int]', a4: 'List[int]'):
    a3 = [0] + a3
    a4 = [0] + a4
    v3 = [0]
    for v4, v5 in zip(a3[1:], accumulate(a4[1:], add)):
        v3.append(max(v5 - v4, v3[-1]))
    v6 = [0]
    for v4, v7 in zip(reversed(a3), accumulate(reversed(a4), add)):
        v6.append(max(v7 - (a2 - v4), v6[-1]))
    v6.reverse()
    v8 = 0
    for v9 in range(a1 + 1):
        v8 = max(v3[v9], v3[v9] - a3[v9] + v6[v9 + 1], v8)
        if v9 != 0:
            v8 = max(v6[v9], v6[v9] - (a2 - a3[v9]) + v3[v9 - 1], v8)
    return v8

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = int(next(v1))
    v4 = [int()] * v2
    v5 = [int()] * v2
    for v6 in range(v2):
        v4[v6] = int(next(v1))
        v5[v6] = int(next(v1))
    v7 = f1(v2, v3, v4, v5)
    if isinstance(v7, Iterable):
        v7 = '\n'.join([str(v5) for v5 in v7])
    print(v7)
if __name__ == '__main__':
    f2()

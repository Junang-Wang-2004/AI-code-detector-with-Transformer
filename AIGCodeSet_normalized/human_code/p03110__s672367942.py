import sys
from math import *
from itertools import *
from collections import *
from functools import *
try:
    from math import gcd
except Exception:
    from fractions import gcd

def f1(a1: int, a2: 'List[float]', a3: 'List[str]'):
    v1 = 0
    for v2, v3 in zip(a2, a3):
        v1 += v2 * {'JPY': 1.0, 'BTC': 380000.0}[v3]
    return v1

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = [float()] * v2
    v4 = [str()] * v2
    for v5 in range(v2):
        v3[v5] = float(next(v1))
        v4[v5] = next(v1)
    v6 = f1(v2, v3, v4)
    print(v6)
if __name__ == '__main__':
    f2()

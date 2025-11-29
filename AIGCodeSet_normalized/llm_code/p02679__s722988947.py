import sys
import math
from collections import defaultdict
from collections import deque
from fractions import Fraction
sys.setrecursionlimit(1000000)
v1 = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
v2 = lambda: int(input())
v3 = lambda: map(int, input().split())
v4 = lambda: list(v3())
v5 = lambda: input()

def f1():
    v1 = v2()
    v2 = defaultdict(int)
    v3, v4 = (0, 0)
    for v5 in range(v1):
        v6, v7 = v3()
        if v6 == v7 == 0:
            v4 += 1
            continue
        if v7 == 0:
            v3 += 1
            continue
        if Fraction(v6, v7) in v2:
            v2[Fraction(v6, v7)] += 1
        else:
            v2[Fraction(v6, v7)] = 1
    v8 = defaultdict(lambda: ())
    v9 = 1
    for v10, v11 in list(v2.items()):
        v6 = v10.numerator
        v7 = v10.denominator
        if v6 > 0:
            if Fraction(-v7, v6) in v2:
                v12 = v2[Fraction(-v7, v6)]
            else:
                v12 = 0
        elif v6 < 0:
            if Fraction(v7, -v6) in v2:
                v12 = v2[Fraction(v7, -v6)]
            else:
                v12 = 0
        else:
            v12 = v3
        v8[v6, v7] = (v11, v12)
    for v11, v12 in list(v8.values()):
        v13 = pow(2, v11, v1) + pow(2, v12, v1) - 1
        v9 = v9 * v13 % v1
    print((v9 + v4 - 1) % v1)
if __name__ == '__main__':
    f1()

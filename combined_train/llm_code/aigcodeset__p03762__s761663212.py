import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, hypot, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
v1 = float('inf')
v2 = 10 ** 9 + 7

def f1(*a1):
    for v1 in a1:
        print(*v1, sep='\n')

def f2(a1):
    return int(a1) - 1

def f3():
    return map(int, input().split())

def f4():
    return map(float, input().split())

def f5():
    return map(f2, input().split())

def f6():
    return list(f3())

def f7():
    return [int(x) - 1 for v1 in input().split()]

def f8():
    return list(f4())

def f9(a1: int):
    return [f13() for v1 in range(a1)]

def f10(a1: int):
    return [f6() for v1 in range(a1)]

def f11(a1: int):
    return [f7() for v1 in range(a1)]

def f12():
    return [list(map(int, l.split())) for v1 in input()]

def f13():
    return int(input())

def f14():
    return float(input())

def f15():
    return input().replace('\n', '')

class C1:

    def __init__(self, a1):
        self.x = a1 % v2

    def __str__(self):
        return str(self.x)
    __repr__ = __str__

    def __add__(self, a1):
        if isinstance(a1, C1):
            return C1(self.x + a1.x)
        else:
            return C1(self.x + a1)
    __radd__ = __add__

    def __sub__(self, a1):
        if isinstance(a1, C1):
            return C1(self.x - a1.x)
        else:
            return C1(self.x - a1)

    def __rsub__(self, a1):
        if isinstance(a1, C1):
            return C1(a1.x - self.x)
        else:
            return C1(a1 - self.x)

    def __mul__(self, a1):
        if isinstance(a1, C1):
            return C1(self.x * a1.x)
        else:
            return C1(self.x * a1)
    __rmul__ = __mul__

    def __truediv__(self, a1):
        if isinstance(a1, C1):
            return C1(self.x * pow(a1.x, v2 - 2, v2))
        else:
            return C1(self.x * pow(a1, v2 - 2, v2))

    def __rtruediv(self, a1):
        if isinstance(a1, self):
            return C1(a1 * pow(self.x, v2 - 2, v2))
        else:
            return C1(a1.x * pow(self.x, v2 - 2, v2))

    def __pow__(self, a1):
        if isinstance(a1, C1):
            return C1(pow(self.x, a1.x, v2))
        else:
            return C1(pow(self.x, a1, v2))

    def __rpow__(self, a1):
        if isinstance(a1, C1):
            return C1(pow(a1.x, self.x, v2))
        else:
            return C1(pow(a1, self.x, v2))

def f17():
    v1, v2 = f3()
    v3 = f6()
    v4 = f6()
    v5 = C1(0)
    for v6, v7 in enumerate(v3[:-1]):
        for v8, v9 in enumerate(v4[:-1]):
            v10 = (v3[v6 + 1] - v7) * (v4[v8 + 1] - v9)
            print(v10, (v6 + 1) * (v1 - (v6 + 1)) * (v8 + 1) * (v2 - (v8 + 1)) * v10)
            v5 += (v6 + 1) * (v1 - (v6 + 1)) * (v8 + 1) * (v2 - (v8 + 1)) * v10
    print(v5)
if __name__ == '__main__':
    f17()

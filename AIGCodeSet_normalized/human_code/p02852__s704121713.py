import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
v1 = 10 ** 9 + 7

def f1():
    return map(int, input().split())

def f2():
    return map(lambda x: int(x) - 1, input().split())

def f3():
    return list(f1())

def f4(a1):
    return [f3() for v1 in range(a1)]

def f5(a1, a2):
    return [a1 for v1 in range(a2)]

def f6(a1, a2, a3):
    return [[a1 for v1 in range(a3)] for v1 in range(a2)]

class C1:

    def __init__(self, a1, a2=None):
        self.f = a1
        self.v = a2

    def __str__(self):
        return str(self.v)

    def ud(self, a1):
        if a1 is None:
            return
        if self.v is None:
            self.v = a1
            return
        self.v = self.f(self.v, a1)

def f8():
    v1, v2 = f1()
    v3 = input().strip()[::-1]
    v4 = []
    v5 = 0
    v6 = 1
    for v7 in v3[1:]:
        if v7 == '0':
            v5 = v6
        v6 += 1
        if v6 > v2:
            if v5 == 0:
                print(-1)
                return
            v4.append(str(v5))
            v6 -= v5
            v5 = 0
    if v5 != 0:
        v4.append(str(v5))
    print(' '.join(v4[::-1]))
if __name__ == '__main__':
    f8()

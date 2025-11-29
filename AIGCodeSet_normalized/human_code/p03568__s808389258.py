import sys

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    return int(f1())

def f3():
    return list(map(int, f1().split()))

def f4():
    return list(map(lambda x: x - 1, f3()))

def f5(a1, a2, a3=0):
    return [[a3] * a2 for v1 in range(a1)]

def f6(a1, a2, a3, a4=0):
    return [f5(a2, a3, a4) for v1 in range(a1)]

def f7(a1: int) -> str:
    return format(a1, 'b')

def f8(a1: int) -> str:
    return format(a1, 'o')

def f9(a1: int) -> str:
    return format(a1, 'x')
v1 = 10 ** 9 + 7

def f10(a1, a2) -> int:
    return -(-a1 // a2)

def f11(a1, a2) -> int:
    return a1 // a2

def f12(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f13(a1, a2):
    return a1 * a2 // f12(a1, a2)

def f14(a1):
    """Return a tuple list of divisor of n"""
    return [(i, a1 // i) for v1 in range(1, int(a1 ** 0.5) + 1) if a1 % v1 == 0]

def f15(a1=10 ** 3):
    """Return a list of prime numbers n or less"""
    v1 = [True] * (a1 + 1)
    v1[0] = v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if not v1[v2]:
            continue
        for v3 in range(v2 * 2, a1 + 1, v2):
            v1[v3] = False
    return [v2 for v2 in range(a1 + 1) if v1[v2]]
from itertools import accumulate as acc
from collections import deque, Counter
from heapq import heapify, heappop, heappush
from bisect import bisect_left

def f16():
    v1 = f2()
    v2 = f3()
    v3 = 3 ** v1
    v4 = list(acc([2 if a % 2 == 0 else 1 for v5 in v2], lambda x, y: x * y))
    print(v3 - v4[-1])
if __name__ == '__main__':
    f16()

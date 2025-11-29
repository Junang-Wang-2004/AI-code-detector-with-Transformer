import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
from math import floor, sqrt, factorial, hypot, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import gcd
from random import randint

def f1(a1, a2):
    return (a1 + a2 - 1) // a2
v1 = float('inf')
v2 = 10 ** 9 + 7

def f2(*a1):
    for v1 in a1:
        print(*v1, sep='\n')

def f3(a1):
    return int(a1) - 1

def f4():
    return map(int, input().split())

def f5():
    return map(float, input().split())

def f6():
    return map(f3, input().split())

def f7():
    return list(f4())

def f8():
    return [int(x) - 1 for v1 in input().split()]

def f9():
    return list(f5())

def f10(a1: int):
    return [f14() for v1 in range(a1)]

def f11(a1: int):
    return [f7() for v1 in range(a1)]

def f12(a1: int):
    return [f8() for v1 in range(a1)]

def f13():
    return [list(map(int, l.split())) for v1 in input()]

def f14():
    return int(input())

def f15():
    return float(input())

def f16():
    return input().replace('\n', '')

def f17():
    v1, v2 = f4()
    v3 = f11(v1)
    v4, v5, v6 = [1 << i for v7 in range(3)]

    def f(a1):
        a1, v2, v3 = a1
        return abs(a1) + abs(v2) + abs(v3)
    v8 = 0
    for v9 in range(1 << 3):
        v10 = bool(v4 & v9)
        v11 = bool(v5 & v9)
        v12 = bool(v6 & v9)
        v3.sort(reverse=True, key=lambda x: (-1) ** v10 * x[0] + (-1) ** v11 * x[1] + (-1) ** v12 * x[2])
        v13, v14, v15 = (0, 0, 0)
        for v16, v17, v18 in v3[:v2]:
            v13 += v16
            v14 += v17
            v15 += v18
        v8 = max(v8, f((v13, v14, v15)))
    print(v8)
if __name__ == '__main__':
    f17()

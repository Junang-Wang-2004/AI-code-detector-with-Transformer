import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub
sys.setrecursionlimit(100000)
input = sys.stdin.readline
v1 = 2 ** 62 - 1

def f1():
    return int(input())

def f2():
    return list(map(int, input().split()))

def f3():
    return float(input())

def f4():
    return list(map(float, input().split()))

def f5():
    return input().strip()

def f6():
    return list(map(str, input().split()))

def f7(*a1):
    print(*a1, file=sys.stderr)

def f8(a1):
    import time

    def wrap(*a1, **a2):
        v1 = time.time()
        v2 = a1(*a1, **a2)
        v3 = time.time()
        f7(v3 - v1, 'sec')
        return v2
    return wrap

@f8
def f10(a1, a2):
    v1 = a1 // 2
    v2 = [defaultdict(lambda: -v1)] * 2
    v2[0][0] = 0
    for v3, v4 in enumerate(a2):
        v5 = [defaultdict(lambda: -v1)] * 2
        v6 = v1 - (a1 - v3) // 2
        v5[0] = v2[1]
        for v7, v8 in v2[0].items():
            if v7 + 1 >= v6:
                v5[1][v7 + 1] = max(v5[1][v7 + 1], v8 + v4)
            if v7 + 2 >= v6:
                v5[0][v7] = max(v5[0][v7], v8)
        v2 = v5
    return max(v2[0][v1], v2[1][v1])

def f11():
    v1 = f1()
    v2 = f2()
    print(f10(v1, v2))
if __name__ == '__main__':
    f11()

from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
from fractions import gcd
import sys

def f1():
    return sys.stdin.readline().rstrip()

def f2():
    return int(f1())

def f3():
    return map(int, f1().split())

def f4():
    return list(map(int, f1().split()))

def f5():
    return tuple(map(int, f1().split()))

def f6(a1):
    return [f2() for v1 in range(a1)]

def f7(a1):
    return [f4() for v1 in range(a1)]

def f8(a1):
    return [f5() for v1 in range(a1)]

def f9():
    return f1()

def f10():
    return f1().split()

def f11():
    return list(f1())

def f12(a1):
    return [f9() for v1 in range(a1)]

def f13(a1):
    return [f10() for v1 in range(a1)]

def f14(a1):
    return [f11() for v1 in range(a1)]
sys.setrecursionlimit(10 ** 6)
v1 = 10 ** 9 + 7
v2 = float('inf')
v3, v4, v5, v6 = f3()
if v3 >= v6:
    print(v6)
elif v3 + v4 >= v6:
    print(v3)
else:
    print(v3 - v6 + v3 + v4)

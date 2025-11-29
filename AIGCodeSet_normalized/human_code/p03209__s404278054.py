import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd

def f1(*a1):
    if debugmode:
        print(*a1)

def f2():
    return sys.stdin.readline().strip()

def f3():
    return f2()

def f4():
    return int(f2())

def f5():
    return float(f2())

def f6():
    return map(int, f2().split())

def f7():
    return map(str, f2().split())

def f8():
    return list(map(int, f2().split()))

def f9():
    return list(map(str, f2().split()))

def f10(a1, a2):
    return a1 * a2 // gcd(a1, a2)
sys.setrecursionlimit(10 ** 9)
v1 = sys.maxsize
v2 = 10 ** 9 + 7
v3 = [0, 0, 1, -1, 1, -1, -1, 1]
v4 = [1, -1, 0, 0, 1, -1, 1, -1]
v5 = False

def f11(a1, a2):
    f1(a1, a2)
    if a1 == 0 and a2 == 1:
        return 1
    elif a1 == 0 and a2 <= 0:
        return 0
    v1 = num[a1 - 1]
    if a2 <= v1 + 1:
        v2 = f11(a1 - 1, a2 - 1)
        f1('a', a1, a2, v2)
        return v2
    elif a2 == v1 + 2:
        v2 = f11(a1 - 1, a2 - 2)
        f1('b', a1, a2, v2 + 1)
        return v2 + 1
    else:
        v3 = num2[a1 - 1]
        f1('tmp1', v3)
        if a2 == v1 * 2 + 3:
            f1('aa', a2 - v1 - 3)
            v4 = f11(a1 - 1, a2 - v1 - 3)
        else:
            v4 = f11(a1 - 1, a2 - v1 - 2)
        f1('c', a1, a2, v3 + 1 + v4)
        return v3 + 1 + v4
v6, v7 = f6()
v8 = [1]
for v9 in range(2, v6 + 1):
    v8.append(2 * v8[-1] + 3)
v10 = [1]
for v9 in range(2, v6 + 1):
    v10.append(2 * v10[-1] + 1)
f1(v8)
f1(v10)
v11 = f11(v6, v7)
print(v11)

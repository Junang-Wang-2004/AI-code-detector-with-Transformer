import math
import itertools

def f1(a1):
    if a1 <= 1:
        return 1
    return a1 * f1(a1 - 1)

def f2(a1, a2):
    return math.floor(f1(a1) / f1(a1 - a2))
from math import *

def f3(a1, a2):
    v1 = 1
    v2 = 1
    if a1 - a2 < a2:
        a2 = a1 - a2
    if a2 != 0:
        while a2:
            v1 *= a1
            v2 *= a2
            v4 = gcd(v1, v2)
            v1 //= v4
            v2 //= v4
            a1 -= 1
            a2 -= 1
    else:
        v1 = 1
    print(v1)
v1 = int(input())
v2 = 1000000007
v3 = f2(v1, 2)
v4 = (10 ** (v1 - 2) - v3) % v2
print(v3 * v4 % v2)

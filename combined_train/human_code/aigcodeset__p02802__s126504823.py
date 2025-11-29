import sys
sys.setrecursionlimit(1000000000)
import math
from fractions import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import defaultdict
from pprint import pprint
v1 = lambda: int(input())
v2 = lambda: map(int, input().split())
v3 = lambda: list(v2())
v4 = float('inf')
v5 = 10 ** 9 + 7

def f1(a1, a2, a3):
    while abs(a2 - a3) > 1:
        v1 = (a2 + a3) // 2
        if a1(v1):
            a2 = v1
        else:
            a3 = v1
    return a2

def f2():
    v1, v2 = v2()
    v3 = set()
    v4 = defaultdict(int)
    for v5 in range(v2):
        v6, v7 = input().split()
        v6 = int(v6)
        if v7 == 'AC':
            v3.add(v6)
        elif v6 not in v3:
            v4[v6] += 1
    print(len(v3), sum((v4[v6] for v6 in v3)))
f2()

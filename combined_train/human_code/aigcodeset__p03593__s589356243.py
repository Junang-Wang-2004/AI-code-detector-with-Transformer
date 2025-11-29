from fractions import gcd
from itertools import combinations, permutations, accumulate
from collections import deque, defaultdict, Counter
import decimal
import re
import sys
sys.setrecursionlimit(10000000)
v1 = 10 ** 9 + 7

def f1():
    return list(map(int, input().split()))

def f2():
    return int(input())
v2, v3 = f1()
v4 = ''
for v5 in range(v2):
    v4 += input()
v6 = Counter(v4)
if v2 % 2 == 0 and v3 % 2 == 0:
    for v7, v8 in v6.items():
        if v8 % 4:
            print('No')
            exit()
elif v2 % 2 == 0 and v3 % 2 or (v2 % 2 and v3 % 2 == 0):
    v9 = 0
    for v7, v8 in v6.items():
        if v8 % 2 or v8 % 4 == 3:
            print('No')
            exit()
        if v8 % 4 == 2:
            v9 += 1
    if v2 % 2 == 0:
        if v9 > v2 // 2:
            print('No')
            exit()
    elif v9 > v3 // 2:
        print('No')
        exit()
else:
    v10 = 0
    v9 = 0
    for v7, v8 in v6.items():
        if v8 % 4 == 1:
            v10 += 1
        if v8 % 4 == 2:
            v9 += 1
        if v8 % 4 == 3:
            print('No')
            exit()
    if v10 != 1:
        print('No')
        exit()
    if v9 > (v2 - 1) // 2 + (v3 - 1) // 2:
        print('No')
        exit()
print('Yes')

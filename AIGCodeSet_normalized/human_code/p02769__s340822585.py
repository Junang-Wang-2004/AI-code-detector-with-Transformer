import sys
sys.setrecursionlimit(1 << 25)
v1 = sys.stdin.readline
v2 = range
v3 = enumerate

def f1():
    return list(map(int, v1().split()))

def f2():
    return int(v1())

def f3(a1):
    """
    H is number of rows
    """
    v1 = []
    for v2 in range(a1):
        v1.append(tuple(map(int, v1().split())))
    return v1

def f4(a1):
    """
    H is number of rows
    A列、B列が与えられるようなとき
    ex1)A,B=read_col(H)    ex2) A,=read_col(H) #一列の場合
    """
    v1 = []
    for v2 in range(a1):
        v1.append(list(map(int, v1().split())))
    return tuple(map(list, zip(*v1)))

def f5(a1):
    """
    H is number of rows
    """
    v1 = []
    for v2 in range(a1):
        v1.append(list(map(int, v1().split())))
    return v1
v4 = 10 ** 9 + 7
v5 = 2 ** 31
from collections import defaultdict, Counter, deque
from operator import itemgetter
from itertools import product, permutations, combinations
from bisect import bisect_left, bisect_right

def f6(a1, a2, a3):
    a2 = min(a2, a1 - a2)
    v2 = v3 = 1
    for v4 in range(a2):
        v2 = v2 * (a1 - v4) % a3
        v3 = v3 * (v4 + 1) % a3
    return v2 * pow(v3, a3 - 2, a3) % a3

def f7(a1, a2, a3):
    v1 = [1]
    if a2 > a1:
        return 0
    v2 = v3 = 1
    for v4 in range(a2):
        v2 = v2 * (a1 - v4) % a3
        v3 = v3 * (v4 + 1) % a3
        v1.append(v2 * pow(v3, a3 - 2, a3) % a3)
    return v1
v4 = 10 ** 9 + 7
v6, v7 = f1()
if v6 <= v7:
    print(f6(v6 + v6 - 1, v6, v4))
    exit()
v8 = 1
v9 = f7(v6, v7, v4)
v10 = f7(v6 - 1, v7, v4)
for v11 in range(1, v7 + 1):
    v8 += v9[v11] * v10[v11]
    v8 %= v4
print(v8)

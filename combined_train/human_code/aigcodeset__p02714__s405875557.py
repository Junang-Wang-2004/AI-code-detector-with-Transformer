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

def f4(a1, a2):
    """
    H is number of rows
    n_cols is number of cols
    A列、B列が与えられるようなとき
    """
    v1 = [[] for v2 in range(a2)]
    for v2 in range(a1):
        v3 = list(map(int, v1().split()))
        for v4 in range(a2):
            v1[v4].append(v3[v4])
    return v1

def f5(a1):
    """
    H is number of rows
    """
    v1 = []
    for v2 in range(a1):
        v1.append(list(map(int, v1().split())))
    return v1

def f6(a1):
    """
    H is number of rows
    文字列で与えられた盤面を読み取る用
    """
    return [v1()[:-1] for v1 in range(a1)]

def f7(a1):
    """
    #→1,.→0として読み込む
    """
    v1 = []
    for v2 in range(a1):
        v1.append([1 if s == '#' else 0 for v3 in v1()[:-1]])
    return v1
v4 = 10 ** 9 + 7
v5 = 2 ** 31
from collections import defaultdict, Counter, deque
from operator import itemgetter
from itertools import product, permutations, combinations
from bisect import bisect_left, bisect_right
from math import gcd

def f8(a1, a2):
    v1 = gcd(a1, a2)
    return a1 * a2 // v1
v6 = f2()
v7 = v1()[:-1]
v8 = v7.count('R')
v9 = v7.count('G')
v10 = v7.count('B')
v11 = {'R': v8, 'G': v9, 'B': v10}
v12 = 0
for v13 in v7:
    v11[v13] -= 1
    if v13 == 'R':
        v14 = v11['G'] * v11['B']
    elif v13 == 'G':
        v14 = v11['R'] * v11['B']
    if v13 == 'B':
        v14 = v11['G'] * v11['R']
    v12 += v14
v15 = 0
for v16 in v2(1, v6 + 1):
    if v16 * 2 >= v6:
        break
    for v17 in v2(v6):
        v18 = v17 + v16
        v19 = v18 + v16
        if v19 >= v6:
            break
        if v7[v17] != v7[v18] and v7[v18] != v7[v19] and (v7[v19] != v7[v17]):
            v15 += 1
print(v12 - v15)

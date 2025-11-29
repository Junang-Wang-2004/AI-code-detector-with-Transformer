def f1():
    v1, v2, v3 = f9()
    v1, v2 = (v2, v1)
    v1, v3 = (v3, v1)
    print(v1, v2, v3)
    return

def f2():
    v1, v2 = f9()
    v3 = f9()
    v4 = (sum(v3) - 1) // (4 * v2) + 1
    v5 = 0
    for v6 in v3:
        if v6 >= v4:
            v5 += 1
    if v5 >= v2:
        print('Yes')
    else:
        print('No')
    return

def f3():
    v1, v2 = f9()
    v3 = v1 % v2
    if v2 - v3 < v3:
        v3 = v2 - v3
    print(v3)
    return

def f4():

    def bfs(a1):
        v1 = [''] * a1
        v2 = deque()
        for v3 in range(1, 10):
            v2.append(str(v3))
            v1[v3 - 1] = str(v3)
        v3 = 9
        while v3 < a1:
            v4 = v2.popleft()
            v5 = v4[-1]
            for v6 in [-1, 0, 1]:
                v7 = int(v5) + v6
                if 0 <= v7 <= 9:
                    v1[v3] = v4 + str(v7)
                    v2.append(v1[v3])
                    v3 += 1
                    if v3 == a1:
                        break
        return v1
    v1 = f8()
    if v1 <= 12:
        v2 = v1
        print(v2)
        return
    v2 = bfs(v1)[-1]
    print(v2)
    return

def f6():
    v1, v2, v3 = f9()
    v4 = f12()
    v5 = set()
    v6 = set()
    v7 = -inf
    for v8, v9 in enumerate(v4):
        if v9 == 'x':
            continue
        if v7 + v3 >= v8:
            continue
        v5.add(v8)
        v7 = v8
    if len(v5) > v2:
        print()
        return
    v7 = inf
    for v8 in range(v1)[::-1]:
        v9 = v4[v8]
        if v9 == 'x':
            continue
        if v7 - v3 <= v8:
            continue
        v6.add(v8)
        v7 = v8
    v10 = []
    for v8 in v5:
        if v8 in v6:
            v10.append(v8 + 1)
    for v11 in sorted(v10):
        print(v11)
    return

def f7():
    v1 = f8()
    v2 = 0
    print(v2)
    return
import sys, bisect, itertools, heapq, math, random
from copy import deepcopy
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque

def f8():
    return int(sys.stdin.readline())

def f9():
    return list(map(int, sys.stdin.readline().split()))

def f10():
    return list(map(str, sys.stdin.readline().split()))

def f11():
    return sys.stdin.readline().split()

def f12():
    return sys.stdin.readline().strip()
global mod, mod2, inf, alphabet, _ep
v1 = 10 ** 9 + 7
v2 = 998244353
v3 = 10 ** 18
v4 = 10 ** (-12)
v5 = [chr(ord('a') + i) for v6 in range(26)]
sys.setrecursionlimit(10 ** 6)
if __name__ == '__main__':
    f6()
'\n\n'

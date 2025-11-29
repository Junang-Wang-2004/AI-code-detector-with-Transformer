import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil, pi, factorial
from operator import itemgetter
import copy

def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return list(map(int, input().split()))

def f4():
    return [int(input()) for v1 in range(n)]

def f5():
    return [[f3()] for v1 in range(n)]

def f6():
    return input().rstrip()

def f7(a1):
    print('\n'.join(a1))

def f8(a1):
    print('\n'.join(list(map(str, a1))))
v1 = 10 ** 17
v2 = 10 ** 9 + 7
v3 = f1()
v4 = [50 for v5 in range(50)]
v6 = []
for v5 in range(50):
    v7 = -v1
    for v8 in range(50):
        if v4[v8] >= v7:
            v7 = v4[v8]
            v9 = v8
    for v8 in range(50):
        v4[v8] += 1
    v4[v9] -= 51
    v6.append(copy.deepcopy(v4))
v10 = v3 % 50
v11 = v3 // 50
v12 = v6[50 - v10 - 1]
for v5 in range(50):
    v12[v5] += v11
print(50)
print(*v12)

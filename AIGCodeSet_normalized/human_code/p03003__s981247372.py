import itertools
from collections import deque, defaultdict, Counter
from itertools import accumulate
import bisect
from heapq import heappop, heappush, heapify
from fractions import gcd
from copy import deepcopy
import math
import queue
v1 = 1000000007
import sys
sys.setrecursionlimit(1000000)

def f1(a1):
    if not isinstance(a1, int):
        raise TypeError('n is not int')
    if a1 < 2:
        raise ValueError('n is not effective')
    v1 = [1] * (a1 + 1)
    for v2 in range(2, int(math.sqrt(a1)) + 1):
        if v1[v2] == 1:
            for v3 in range(2 * v2, a1 + 1):
                if v3 % v2 == 0:
                    v1[v3] = 0
    v4 = []
    for v2 in range(2, a1 + 1):
        if v1[v2] == 1:
            v4.append(v2)
    return v4

def f2(a1):
    if a1 == 1:
        return 1
    else:
        return a1 * f2(a1 - 1)

class C1:

    def __init__(self, a1):
        self.parent = [i for v1 in range(a1 + 1)]
        self.rank = [0 for v1 in range(a1 + 1)]

    def findroot(self, a1):
        if a1 == self.parent[a1]:
            return a1
        else:
            v1 = self.parent[a1]
            v1 = self.findroot(self.parent[a1])
            return v1

    def union(self, a1, a2):
        v1 = self.findroot(a1)
        v2 = self.findroot(a2)
        if v1 < v2:
            self.parent[v2] = v1
        else:
            self.parent[v1] = v2

    def same_group_or_no(self, a1, a2):
        return self.findroot(a1) == self.findroot(a2)

def f6():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = list(map(int, input().split()))
    v5 = [[0] * (v2 + 2) for v6 in range(v1 + 2)]
    v7 = [[0] * (v2 + 2) for v6 in range(v1 + 2)]
    v5[0][0] = 1
    v7[1][1] = 1
    for v6 in range(v1 + 1):
        for v8 in range(v2 + 1):
            if v6 == 0 and v8 == 0:
                continue
            if v6 >= 1 and v8 >= 1 and (v3[v6 - 1] == v4[v8 - 1]):
                v5[v6][v8] = v7[v6][v8] % v1
            v7[v6 + 1][v8 + 1] = (v7[v6 + 1][v8] + v7[v6][v8 + 1] - v7[v6][v8] + v5[v6][v8]) % v1
    print(v7[v1 + 1][v2 + 1] % v1)
if __name__ == '__main__':
    f6()

from collections import deque, defaultdict, Counter
from itertools import accumulate
import bisect
from heapq import heappop, heappush
from fractions import gcd
from copy import deepcopy
import math
import queue
v1 = 1000000007

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
    v1 = int(input())
    v2 = map(int, input().split())
    v3 = len(set(v2))
    if (v1 - v3) % 2 == 0:
        print(v3)
    else:
        print(v3 - 1)
if __name__ == '__main__':
    f6()

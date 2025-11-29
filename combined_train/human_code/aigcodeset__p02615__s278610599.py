import re
import math
from collections import defaultdict, deque, Counter
from fractions import Fraction
import bisect
import itertools
from itertools import accumulate
from copy import deepcopy
import heapq
import random
import time
import os
import sys
from functools import lru_cache, reduce
v1 = sys.stdin.readline
sys.setrecursionlimit(100000)
v2 = 'abcdefghijklmnopqrstuvwxyz'
v3 = '0123456789'
v4 = int(10 ** 9 + 7)
v5 = int(10 ** 19)

class C1:

    def __init__(self, a1=[]):
        self.heap = []
        self.dic = defaultdict(bool)
        self.size = 0
        for v1 in a1:
            self.add(v1)

    def __str__(self):
        return str(self.heap)

    def add(self, a1):
        if not self.find(a1):
            heapq.heappush(self.heap, a1)
            self.dic[a1] = True
            self.size += 1

    def remove(self, a1):
        if self.find(a1):
            self.dic[a1] = False
            self.size -= 1

    def find(self, a1):
        return self.dic[a1]

    def top(self):
        while self.heap and self.dic[self.heap[0]] == False:
            heapq.heappop(self.heap)
        if self.heap:
            return self.heap[0]
        else:
            return None

    def pop(self):
        v1 = None
        if self.heap:
            v1 = self.top()
            self.remove(v1)
        return v1

class C2:

    def __init__(self, a1=[]):
        self.heap = []
        self.dic = defaultdict(int)
        self.size = 0
        for v1 in a1:
            self.add(v1)

    def __str__(self):
        return str(self.heap)

    def add(self, a1):
        heapq.heappush(self.heap, a1)
        self.dic[a1] += 1
        self.size += 1

    def remove(self, a1):
        if self.dic[a1] > 0:
            self.dic[a1] -= 1
            self.size -= 1

    def count(self, a1):
        return self.dic[a1]

    def find(self, a1):
        return self.dic[a1] > 0

    def top(self):
        while self.heap and self.dic[self.heap[0]] == 0:
            heapq.heappop(self.heap)
        if self.heap:
            return self.heap[0]
        else:
            return None

    def pop(self):
        v1 = None
        if self.heap:
            v1 = self.top()
            self.remove(v1)
        return v1

class C3:

    def __init__(self, a1, a2, a3=1):
        self.x = a1
        self.y = a2
        self.val = a3

class C4:

    def __init__(self, a1):
        self.n = a1
        self.P = [a for v1 in range(a1)]
        self.rank = [0] * a1

    def find(self, a1):
        if a1 != self.P[a1]:
            self.P[a1] = self.find(self.P[a1])
        return self.P[a1]

    def same(self, a1, a2):
        return self.find(a1) == self.find(a2)

    def link(self, a1, a2):
        if self.rank[a1] < self.rank[a2]:
            self.P[a1] = a2
        elif self.rank[a2] < self.rank[a1]:
            self.P[a2] = a1
        else:
            self.P[a1] = a2
            self.rank[a2] += 1

    def unite(self, a1, a2):
        self.link(self.find(a1), self.find(a2))

    def size(self):
        v1 = set()
        for v2 in range(self.n):
            v1.add(self.find(v2))
        return len(v1)

def f17(a1):
    print('yes' if a1 else 'no')

def f18(a1):
    print('Yes' if a1 else 'No')

def f19(a1):
    print('YES' if a1 else 'NO')

def f20(a1, a2):
    v1 = a2
    while v1 < a1:
        v1 *= a2
    return v1 == a1

def f21(a1, a2):
    v1 = [0] * a2
    for v2 in range(a2):
        if a1 >> a2 - v2 - 1 & 1 == 1:
            v1[v2] = 1
        else:
            v1[v2] = 0
    return v1

def f22(a1, a2=0):
    v1 = [1] * (a1 + 1)
    for v2 in range(2, len(v1)):
        v1[v2] = v1[v2 - 1] * v2
        if a2 > 0:
            v1[v2] %= a2
    return v1

def f23(a1, a2, a3, a4):
    if a1 - a2 < 0:
        return 0
    return a4[a1] * pow(a4[a1 - a2], a3 - 2, a3) * pow(a4[a2], a3 - 2, a3) % a3

def f24(a1, a2):
    v1 = a1 & -a1
    v2 = a1 + v1
    v3 = a1 & ~v2
    v3 //= v1
    v3 = v3 >> 1
    a1 = v2 | v3
    if a1 >= 1 << a2:
        return False
    else:
        return a1

def f25(a1):
    if a1 == 0:
        return []
    v1 = [True] * (a1 + 1)
    v1[0] = False
    v1[1] = False
    for v2 in range(2, a1 + 1):
        if v1[v2]:
            for v3 in range(v2 * 2, a1 + 1, v2):
                v1[v3] = False
    v4 = []
    for v2 in range(a1 + 1):
        if v1[v2]:
            v4.append(v2)
    return v4

def f26(a1):
    if a1 <= 1:
        return False
    v1 = 2
    while v1 * v1 <= a1:
        if a1 % v1 == 0:
            return False
        v1 += 1
    return True

def f27(a1, a2, a3):
    return a2 if a1 else a3

def f28(a1):
    v1 = 2
    v2 = defaultdict(int)
    while v1 * v1 <= a1:
        while a1 % v1 == 0:
            a1 //= v1
            v2[v1] += 1
        v1 += 1
    if a1 > 1:
        v2[a1] += 1
    return v2

def f29(a1=1):
    if a1 == 1:
        v1 = list(map(int, input().split()))
    else:
        v1 = [None] * a1
        for v2 in range(a1):
            v1[v2] = int(input())
    return v1

def f30(a1=1):
    if a1 == 1:
        v1 = list(map(float, input().split()))
    else:
        v1 = [None] * a1
        for v2 in range(a1):
            v1[v2] = float(input())
    return v1

def f31(a1):
    v1 = True
    v2 = min(a1) - 1
    for v3 in a1:
        if v2 >= v3:
            v1 = False
        v2 = v3
    return v1

def f32(a1):
    v1 = True
    v2 = min(a1) - 1
    for v3 in a1:
        if v2 > v3:
            v1 = False
        v2 = v3
    return v1

def f33(a1):
    v1 = sum(a1)
    v2 = defaultdict(int)
    v2[0] = 1
    for v3 in range(0, len(a1)):
        for v4 in range(v1, -1, -1):
            if v4 - a1[v3] >= 0:
                v2[v4] += v2[v4 - a1[v3]]
    return v2

def f34(a1):
    v1 = deepcopy(a1)
    for v2 in a1:
        if not v2.x == v2.y:
            v1.append(C3(v2.y, v2.x, v2.val))
    return v1

def f35(a1, a2, a3):
    v1 = [v5] * a2
    v2 = [[] for v3 in range(a2)]
    for v4 in a1:
        v2[v4.x].append([v4.val, v4.y])
    v5 = PriorityQueue()
    v5.put([0, a3])
    while not v5.empty():
        v6, v7 = v5.get()
        if v1[v7] == v5:
            v1[v7] = v6
            for v8, v9 in v2[v7]:
                v10 = v6 + v8
                v5.put([v10, v9])
    return v1

def f36(a1, a2):
    v1 = [[v5 for v2 in range(a2)] for v3 in range(a2)]
    for v3 in range(a2):
        v1[v3][v3] = 0
    for v4 in a1:
        v1[v4.x][v4.y] = min(v1[v4.x][v4.y], v4.val)
    for v5 in range(a2):
        for v6 in range(a2):
            for v7 in range(a2):
                if v1[v6][v5] == v5 or v1[v5][v7] == v5:
                    continue
                v1[v6][v7] = min(v1[v6][v7], v1[v6][v5] + v1[v5][v7])
    return v1

def f37(a1, a2, a3):
    v1 = [v5] * a2
    v1[a3] = 0
    for v2 in range(a2):
        for v3 in a1:
            if v1[v3.x] == v5:
                continue
            v1[v3.y] = min(v1[v3.y], v1[v3.x] + v3.val)
    return v1

def f38(a1, a2, a3, a4):
    return abs(a1 - a3) + abs(a2 - a4)

def f39(a1, a2, a3, a4):
    return math.sqrt((a1 - a3) ** 2 + (a2 - a4) ** 2)

class C5:

    def __init__(self, a1, a2, a3, a4):
        self.V = a2
        self.used = [False] * a2
        self.G = [[] for v1 in range(a2)]
        self.s = a3
        self.t = a4
        for v2 in a1:
            self.G[v2.x].append({'x': v2.x, 'y': v2.y, 'cap': v2.val, 'rev': len(self.G[v2.y])})
            self.G[v2.y].append({'x': v2.y, 'y': v2.x, 'cap': 0, 'rev': len(self.G[v2.x]) - 1})

    def dfs(self, a1, a2, a3=v5):
        if a1 == a2:
            return a3
        self.used[a1] = True
        for v1 in range(len(self.G[a1])):
            v2 = self.G[a1][v1]['x']
            v3 = self.G[a1][v1]['y']
            v4 = self.G[a1][v1]['cap']
            v5 = self.G[v3][self.G[v2][v1]['rev']]
            if self.used[v3] or v4 == 0:
                continue
            v6 = self.dfs(v3, a2, min(a3, v4))
            if v6 > 0:
                self.G[a1][v1]['cap'] -= v6
                v5['cap'] += v6
                return v6
        return 0

    def maxflow(self):
        v1 = 0
        while True:
            self.used = [False] * V
            v2 = self.dfs(self.s, self.t)
            if v2 == 0:
                break
            v1 += v2
        return v1

def f42(*a1):
    v1 = sorted(zip(*a1))
    for v2 in range(len(a1)):
        for v3 in range(len(v1)):
            a1[v2][v3] = v1[v3][v2]

def f43(*a1):
    v1 = list(zip(*a1))
    v2 = []
    for v3 in range(len(v1) - 1, -1, -1):
        v2.append(v1[v3])
    for v3 in range(len(a1)):
        for v4 in range(len(v2)):
            a1[v3][v4] = v2[v4][v3]
v6 = int(input())
v7 = f29()
v7.sort()
v7.reverse()
v8 = []
v8.append([v7[1], v7[0]])
v8.append([v7[1], v7[0]])
v9 = 0
v10 = v7[0]
for v11 in range(2, v6):
    v12, v13 = v8[v9]
    v8.append([v7[v11], v13])
    v8.append([v7[v11], v12])
    v10 += v12
    v9 += 1
print(v10)

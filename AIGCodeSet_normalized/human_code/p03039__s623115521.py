import re
import math
import fractions
import random
import time
v1 = int(10 ** 9 + 7)
v2 = int(10 ** 20)
v3 = [1] * 250000
for v4 in range(2, 250000):
    v3[v4] = v3[v4 - 1] * v4 % v1

class C1:

    def __init__(self, a1):
        self.n = a1
        self.P = [v4 for v4 in range(N)]
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

def f6(a1, a2):
    v1 = [0] * a2
    for v2 in range(a2):
        if a1 >> a2 - v2 - 1 & 1 == 1:
            v1[v2] = 1
        else:
            v1[v2] = 0
    return v1

def f7(a1, a2):
    return math.factorial(a1) // math.factorial(a1 - a2) // math.factorial(a2)

def f8(a1, a2):
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

def f9(a1, a2):
    return v3[a1] * pow(v3[a1 - a2], v1 - 2, v1) * pow(v3[a2], v1 - 2, v1)

def f10():
    return
v5, v6, v7 = map(int, input().split())
v8 = 0
for v4 in range(1, v5):
    v8 += v6 * v6 * abs(v5 - v4) * v4 * f9(v5 * v6 - 2, v7 - 2)
    v8 %= v1
for v4 in range(1, v6):
    v8 += v5 * v5 * abs(v6 - v4) * v4 * f9(v5 * v6 - 2, v7 - 2)
    v8 %= v1
print(v8)

import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools
import time, random
sys.setrecursionlimit(10 ** 7)
v1 = 10 ** 20
v2 = 1.0 / 10 ** 10
v3 = 10 ** 9 + 7
v4 = 998244353
v5 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
v6 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def f1():
    return list(map(int, sys.stdin.readline().split()))

def f2():
    return [list(map(int, l.split())) for v1 in sys.stdin.readlines()]

def f3():
    return [int(x) - 1 for v1 in sys.stdin.readline().split()]

def f4():
    return [float(x) for v1 in sys.stdin.readline().split()]

def f5():
    return sys.stdin.readline().split()

def f6():
    return int(sys.stdin.readline())

def f7():
    return float(sys.stdin.readline())

def f8():
    return input()

def f9(a1):
    return print(a1, flush=True)

def f10(a1):
    return print(str(a1), file=sys.stderr)

def f11(a1, a2):
    return a2.join(map(str, a1))

def f12(a1, a2, a3):
    return a2.join((a3.join(map(str, b)) for v1 in a1))

class C1:

    def __init__(self, a1, a2, a3):
        if isinstance(a1, list):
            v1 = len(a1)
        else:
            v1 = a1
        v2 = 1
        while 2 ** v2 <= v1:
            v2 += 1
        self.D = a2
        self.H = v2
        self.N = 2 ** v2
        if isinstance(a1, list):
            self.A = [a2] * self.N + a1 + [a2] * (self.N - v1)
            for v2 in range(self.N - 1, 0, -1):
                self.A[v2] = a3(self.A[v2 * 2], self.A[v2 * 2 + 1])
        else:
            self.A = [a2] * (self.N * 2)
        self.F = a3

    def find(self, a1):
        return self.A[a1 + self.N]

    def update(self, a1, a2):
        a1 += self.N
        self.A[a1] = a2
        while a1 > 1:
            a1 = a1 // 2
            self.A[a1] = self.merge(self.A[a1 * 2], self.A[a1 * 2 + 1])

    def merge(self, a1, a2):
        return self.F(a1, a2)

    def total(self):
        return self.A[1]

    def query(self, a1, a2):
        v1 = self.A
        v2 = a1 + self.N
        v3 = a2 + self.N
        v4 = self.D
        while v2 < v3:
            if v2 % 2 == 1:
                v4 = self.merge(v4, v1[v2])
                v2 += 1
            if v3 % 2 == 1:
                v3 -= 1
                v4 = self.merge(v4, v1[v3])
            v2 >>= 1
            v3 >>= 1
        return v4

def f18():
    v1 = f6()
    v2 = f8()
    v3 = f6()
    v4 = [f5() for v5 in range(v3)]
    v6 = [[0] * 26]
    v7 = ord('a')
    for v8 in v2:
        v9 = [0] * 26
        v9[ord(v8) - v7] = 1
        v6.append(v9)

    def f(a1, a2):
        return [a1[i] + a2[i] for v1 in range(26)]
    v10 = C1(v6, [0] * 26, f)
    v11 = []
    for v9, v12, v13 in v4:
        if v9 == '1':
            v14 = [0] * 26
            v14[ord(v13) - v7] = 1
            v10.update(int(v12), v14)
        else:
            v8 = v10.query(0, int(v12))
            v15 = v10.query(0, int(v13) + 1)
            v11.append(len([1 for v16 in range(26) if v8[v16] != v15[v16]]))
    return f11(v11, '\n')
print(f18())

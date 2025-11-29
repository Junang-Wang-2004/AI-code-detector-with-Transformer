import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
from functools import lru_cache
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = 10 ** (-7)

def f1():
    """
    一つの整数
    """
    return int(input())

def f2():
    """
    一行に複数の整数
    """
    return list(map(int, input().split()))

class C1:

    def __init__(self, a1):
        """
        modを指定して初期化
        """
        self.mod = a1
        self.fac = [1, 1]
        self.ifac = [1, 1]
        self.inv = [0, 1]

    def calc(self, a1, a2):
        """
        nCk%modを計算する
        """
        if a2 < 0 or a1 < a2:
            return 0
        self.make_tables(a1)
        a2 = min(a2, a1 - a2)
        return self.fac[a1] * (self.ifac[a2] * self.ifac[a1 - a2] % self.mod) % self.mod

    def make_tables(self, a1):
        """
        階乗テーブル・階乗の逆元テーブルを作成
        """
        for v1 in range(len(self.fac), a1 + 1):
            self.fac.append(self.fac[-1] * v1 % self.mod)
            self.inv.append(-self.inv[self.mod % v1] * (self.mod // v1) % self.mod)
            self.ifac.append(self.ifac[-1] * self.inv[-1] % self.mod)
v2 = 998244353
v4 = C1(v2)
v5, v6, v7 = f2()
v8 = 0
for v9 in range(min(v5, v7 + 1)):
    v8 += v6 * pow(v6 - 1, v5 - 1 - v9, v2) * v4.calc(v5 - 1, v9) % v2
    v8 %= v2
print(v8)

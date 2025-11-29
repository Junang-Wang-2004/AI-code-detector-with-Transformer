import sys
sys.setrecursionlimit(10 ** 7)
v1 = sys.stdin.readline

class C1:

    def __init__(self, a1: int, a2: int):
        self.mod = a2
        self.fact = [0] * (a1 + 1)
        self.factinv = [0] * (a1 + 1)
        self.inv = [0] * (a1 + 1)
        self.fact[0] = self.fact[1] = 1
        self.factinv[0] = self.factinv[1] = 1
        self.inv[1] = 1
        for v1 in range(2, a1 + 1):
            self.fact[v1] = self.fact[v1 - 1] * v1 % a2
            self.inv[v1] = -self.inv[a2 % v1] * (a2 // v1) % a2
            self.factinv[v1] = self.factinv[v1 - 1] * self.inv[v1] % a2

    def ncr(self, a1: int, a2: int):
        if a2 < 0 or a1 < a2:
            return 0
        a2 = min(a2, a1 - a2)
        return self.fact[a1] * self.factinv[a2] % self.mod * self.factinv[a1 - a2] % self.mod

    def nhr(self, a1: int, a2: int):
        return self.ncr(a1 + a2 - 1, a2)

    def npr(self, a1: int, a2: int):
        if a2 < 0 or a1 < a2:
            return 0
        return self.fact[a1] * self.factinv[a1 - a2] % self.mod

def f4():
    v1, v2 = map(int, v1().split())
    v3 = list(map(int, v1().split()))
    v4 = 10 ** 9 + 7
    v3.sort()
    v5 = C1(v1, v4)
    v6 = 0
    for v7 in range(v1):
        v6 += v5.ncr(v7, v2 - 1) * v3[v7] % v4
        v6 -= v5.ncr(v1 - v7 - 1, v2 - 1) * v3[v7] % v4
        v6 %= v4
    print(v6)
if __name__ == '__main__':
    f4()

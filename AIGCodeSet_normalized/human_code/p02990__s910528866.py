import sys
v1 = sys.stdin
sys.setrecursionlimit(10 ** 7)

def f1():
    return map(int, v1.readline().split())

def f2():
    return map(lambda x: int(x) - 1, v1.readline().split())

def f3():
    return map(float, v1.readline().split())

def f4():
    return v1.readline().split()

def f5():
    return v1.readline().rstrip()

def f6():
    return list(f5())

def f7():
    return int(v1.readline())

def f8():
    return float(v1.readline())

class C1(object):

    def __init__(self, a1: int, a2: int):
        self.cap = a1
        self.mod = a2
        self.inv = self._calc_inv()
        self.fac = self._calc_fac()
        self.fac_inv = self._calc_fac_inv()

    def _calc_inv(self):
        v1 = [0, 1]
        for v2 in range(2, self.cap + 1):
            v1.append((self.mod - self.mod // v2 * v1[self.mod % v2]) % self.mod)
        return v1

    def _calc_fac(self):
        v1 = [1]
        for v2 in range(1, self.cap + 1):
            v1.append(v2 * v1[-1] % self.mod)
        return v1

    def _calc_fac_inv(self):
        v1 = [1]
        for v2 in range(1, self.cap + 1):
            v1.append(self.inv[v2] * v1[-1] % self.mod)
        return v1

    def nCr(self, a1: int, a2: int):
        return self.fac[a1] * self.fac_inv[a1 - a2] * self.fac_inv[a2] % self.mod

    def nPr(self, a1: int, a2: int):
        if a2 > a1:
            raise ValueError('n must be larger than r (n={}, r={})'.format(a1, a2))
        return self.fac[a1] * self.fac_inv[a1 - a2] % self.mod

    def nHr(self, a1: int, a2: int):
        return self.nCr(a1 + a2 - 1, a1)
v2, v3 = f1()
v4 = 10 ** 9 + 7
v5 = C1(2 * v2 + 1, v4)
for v6 in range(1, v3 + 1):
    if v2 - v3 - v6 + 1 < 0:
        print(0)
    else:
        print(v5.nHr(v3 - v6, v6) * v5.nHr(v2 - v3 - v6 + 1, v6 + 1) % v4)

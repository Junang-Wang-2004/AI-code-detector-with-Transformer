class C1(object):
    """
        See:
        http://drken1215.hatenablog.com/entry/2018/06/08/210000
    """

    def __init__(self, a1=500050, a2=10 ** 9 + 7):
        self.max_value = a1
        self.mod = a2
        self.fac = [0 for v1 in range(self.max_value)]
        self.finv = [0 for v1 in range(self.max_value)]
        self.inv = [0 for v1 in range(self.max_value)]
        self.fac[0] = 1
        self.fac[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1
        for v2 in range(2, self.max_value):
            self.fac[v2] = self.fac[v2 - 1] * v2 % self.mod
            self.inv[v2] = self.mod - self.inv[self.mod % v2] * (self.mod // v2) % self.mod
            self.finv[v2] = self.finv[v2 - 1] * self.inv[v2] % self.mod

    def count_nCr(self, a1, a2):
        if a1 < a2:
            return 0
        if a1 < 0 or a2 < 0:
            return 0
        return self.fac[a1] * (self.finv[a2] * self.finv[a1 - a2] % self.mod) % self.mod

def f2():
    v1, v2 = map(int, input().split())
    v3 = sorted(list(map(int, input().split())))
    v4 = C1()
    v5 = 0
    for v6, v7 in enumerate(v3):
        v8 = v4.count_nCr(n=v6, r=v2 - 1)
        v5 += v8 * v7
    for v6, v7 in enumerate(v3[::-1]):
        v8 = v4.count_nCr(n=v6, r=v2 - 1)
        v5 -= v8 * v7
    print(v5 % (10 ** 9 + 7))
if __name__ == '__main__':
    f2()

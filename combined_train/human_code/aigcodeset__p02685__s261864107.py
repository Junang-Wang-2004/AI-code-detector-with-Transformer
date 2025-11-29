v1 = 998244353

class C1:

    def __init__(self, a1):
        self.x = a1 % v1 if isinstance(a1, int) else int(a1) % v1

    def __str__(self):
        return str(self.x)
    __repr__ = __str__

    def __iadd__(self, a1):
        self.x += a1.x if isinstance(a1, C1) else a1
        self.x -= v1 if self.x >= v1 else 0
        return self

    def __isub__(self, a1):
        self.x += v1 - a1.x if isinstance(a1, C1) else v1 - a1
        self.x -= v1 if self.x >= v1 else 0
        return self

    def __imul__(self, a1):
        self.x *= a1.x if isinstance(a1, C1) else a1
        self.x %= v1
        return self

    def __imod__(self, a1):
        self.x %= a1.x if isinstance(a1, C1) else a1
        self.x %= v1
        return self

    def __add__(self, a1):
        return C1(self.x + a1.x) if isinstance(a1, C1) else C1(self.x + a1)

    def __sub__(self, a1):
        return C1(self.x - a1.x) if isinstance(a1, C1) else C1(self.x - a1)

    def __mul__(self, a1):
        return C1(self.x * a1.x) if isinstance(a1, C1) else C1(self.x * a1)

    def __mod__(self, a1):
        return C1(self.x % a1.x) if isinstance(a1, C1) else C1(self.x % a1)

    def __truediv__(self, a1):
        return C1(self.x * pow(a1.x, v1 - 2, v1)) if isinstance(a1, C1) else C1(self.x * pow(a1, v1 - 2, v1))

    def __pow__(self, a1):
        return C1(pow(self.x, a1.x, v1)) if isinstance(a1, C1) else C1(pow(self.x, a1, v1))
    __radd__ = __add__

    def __rsub__(self, a1):
        return C1(a1.x - self.x) if isinstance(a1, C1) else C1(a1 - self.x)
    __rmul__ = __mul__

    def __rmod__(self, a1):
        return C1(a1.x % self.x) if isinstance(a1, C1) else C1(a1 % self.x)

    def __rtruediv__(self, a1):
        return C1(a1.x * pow(self.x, v1 - 2, v1)) if isinstance(a1, C1) else C1(a1 * pow(self.x, v1 - 2, v1))

    def __rpow__(self, a1):
        return C1(pow(a1.x, self.x, v1)) if isinstance(a1, C1) else C1(pow(a1, self.x, v1))

class C2:

    def __init__(self, a1):
        self.n = a1
        v1 = [0] * (a1 + 1)
        v2 = [0] * (a1 + 1)
        v1[0] = C1(1)
        for v3 in range(1, a1 + 1):
            v1[v3] = v1[v3 - 1] * v3
        v2[-1] = pow(v1[-1], v1 - 2)
        for v3 in range(a1, 0, -1):
            v2[v3 - 1] = v2[v3] * v3
        self.fact = v1
        self.ifact = v2

    def calc(self, a1, a2):
        if a2 < 0 or a2 > a1:
            return 0
        return self.fact[a1] * self.ifact[a2] * self.ifact[a1 - a2]
v2 = C2(200005)
v3, v4, v5 = map(int, input().split())
v6 = C1(0)
for v7 in range(v5 + 1):
    v8 = C1(v4)
    v8 *= pow(v4 - 1, v3 - 1 - v7, v1)
    v8 *= v2.calc(v3 - 1, v7)
    v6 += v8
print(v6)

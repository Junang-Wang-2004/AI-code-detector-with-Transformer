v1 = input()
v2 = 10 ** 9 + 7

class C1:

    def __init__(self, a1):
        self.x = a1 % v2

    def __str__(self):
        return str(self.x)
    __repr__ = __str__

    def __add__(self, a1):
        return C1(self.x + a1.x) if isinstance(a1, C1) else C1(self.x + a1)

    def __sub__(self, a1):
        return C1(self.x - a1.x) if isinstance(a1, C1) else C1(self.x - a1)

    def __mul__(self, a1):
        return C1(self.x * a1.x) if isinstance(a1, C1) else C1(self.x * a1)

    def __truediv__(self, a1):
        return C1(self.x * pow(a1.x, v2 - 2, v2)) if isinstance(a1, C1) else C1(self.x * pow(a1, v2 - 2, v2))

    def __pow__(self, a1):
        return C1(pow(self.x, a1.x, v2)) if isinstance(a1, C1) else C1(pow(self.x, a1, v2))

    def __radd__(self, a1):
        return C1(a1 + self.x)

    def __rsub__(self, a1):
        return C1(a1 - self.x)

    def __rmul__(self, a1):
        return C1(a1 * self.x)

    def __rtruediv__(self, a1):
        return C1(a1 * pow(self.x, v2 - 2, v2))

    def __rpow__(self, a1):
        return C1(pow(a1, self.x, v2))

def f1(a1):
    return C1(1) if a1 == 0 else C1(3) ** (a1 - 1) + 2 * f1(a1 - 1) if v1[len(v1) - a1] == '1' else f1(a1 - 1)
v3 = f1(len(v1))
print(v3)

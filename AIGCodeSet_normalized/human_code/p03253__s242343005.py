class C1:

    def __init__(self, a1, a2):
        """combination(max_value, all)"""
        v1 = [-1] * (a1 + 1)
        v1[0] = 1
        v1[1] = 1
        for v2 in range(2, a1 + 1):
            v1[v2] = v2 * v1[v2 - 1] % a2
        v3 = [1] * (a1 + 1)
        v3[a1] = pow(v1[a1], a2 - 2, a2)
        for v2 in range(a1 - 1, 0, -1):
            v3[v2] = v3[v2 + 1] * (v2 + 1) % a2
        self.fact = v1
        self.invs = v3
        self.mod = a2

    def combination(self, a1, a2):
        if a1 - a2 < a2:
            return self.combination(a1, a1 - a2)
        if a2 < 0:
            return 0
        if a2 == 0:
            return 1
        if a2 == 1:
            return a1
        return self.fact[a1] * self.invs[a2] * self.invs[a1 - a2] % self.mod

def f2(a1):
    v1 = a1
    v2 = 2
    v3 = 0
    while v1 % v2 == 0:
        v1 //= v2
        v3 += 1
    yield v3
    v2 = 3
    v4 = v2 * v2
    while v4 <= a1:
        v3 = 0
        while v1 % v2 == 0:
            v1 //= v2
            v3 += 1
        yield v3
        v4 += v2 * 4 + 4
        v2 += 2
    if v1 > 1:
        yield 1

def f3():
    v1 = 10 ** 9 + 7
    v2, v3 = map(int, input().split())
    v4 = C1(max_value=v2 + 30, mod=v1)
    v5 = 1
    for v6 in f2(v3):
        v5 = v5 * v4.combination(v2 + v6 - 1, v6) % v1
    print(v5)
if __name__ == '__main__':
    f3()

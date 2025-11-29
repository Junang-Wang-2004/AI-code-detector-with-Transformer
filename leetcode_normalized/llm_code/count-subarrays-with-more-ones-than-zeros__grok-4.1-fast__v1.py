class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 1)

    def update(self, a1, a2):
        while a1 <= self.size:
            self.tree[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.tree[a1]
            a1 -= a1 & -a1
        return v1

class C2:

    def subarraysWithMoreZerosThanOnes(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        if v2 == 0:
            return 0
        v3 = v2 + 1
        v4 = C1(2 * v2 + 2)
        v4.update(v3, 1)
        v5 = 0
        v6 = 0
        for v7 in a1:
            v5 += 1 if v7 == 0 else -1
            v6 = (v6 + v4.query(v3 + v5 - 1)) % v1
            v4.update(v3 + v5, 1)
        return v6

class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 2)

    def update(self, a1, a2):
        a1 += 1
        while a1 <= self.size:
            self.tree[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.tree[a1]
            a1 -= a1 & -a1
        return v2

class C2:

    def goodTriplets(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        for v3, v4 in enumerate(a1):
            v2[v4] = v3
        v5 = [0] * v1
        v6 = C1(v1)
        for v3 in range(v1 - 1, -1, -1):
            v7 = v2[a2[v3]]
            v5[v3] = v6.query(v1 - 1) - v6.query(v7)
            v6.update(v7, 1)
        v8 = 0
        v9 = C1(v1)
        for v3 in range(v1):
            v7 = v2[a2[v3]]
            v10 = v9.query(v7 - 1)
            v8 += v10 * v5[v3]
            v9.update(v7, 1)
        return v8

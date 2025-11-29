class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 2)

    def update(self, a1, a2):
        while a1 <= self.size:
            self.tree[a1] = max(self.tree[a1], a2)
            a1 += a1 & -a1

    def query(self, a1):
        v1 = 0
        while a1 > 0:
            v1 = max(v1, self.tree[a1])
            a1 -= a1 & -a1
        return v1

class C2:

    def minOperations(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = {a1[i]: i + 1 for v3 in range(v1)}
        v4 = C1(v1)
        for v5 in a2:
            if v5 in v2:
                v6 = v2[v5]
                v7 = v4.query(v6 - 1)
                v4.update(v6, v7 + 1)
        v8 = v4.query(v1)
        return v1 - v8

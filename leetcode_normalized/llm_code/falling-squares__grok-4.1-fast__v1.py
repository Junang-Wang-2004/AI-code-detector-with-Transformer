import bisect

class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (4 * a1)
        self.lazy = [float('-inf')] * (4 * a1)

    def propagate(self, a1, a2, a3):
        if self.lazy[a1] != float('-inf'):
            self.tree[a1] = max(self.tree[a1], self.lazy[a1])
            if a2 != a3:
                self.lazy[2 * a1] = max(self.lazy[2 * a1], self.lazy[a1])
                self.lazy[2 * a1 + 1] = max(self.lazy[2 * a1 + 1], self.lazy[a1])
            self.lazy[a1] = float('-inf')

    def update(self, a1, a2, a3, a4=1, a5=0, a6=None):
        if a6 is None:
            a6 = self.size - 1
        self.propagate(a4, a5, a6)
        if a1 > a6 or a2 < a5:
            return
        if a1 <= a5 and a6 <= a2:
            self.lazy[a4] = max(self.lazy[a4], a3)
            self.propagate(a4, a5, a6)
            return
        v2 = (a5 + a6) // 2
        self.update(a1, a2, a3, 2 * a4, a5, v2)
        self.update(a1, a2, a3, 2 * a4 + 1, v2 + 1, a6)
        self.tree[a4] = max(self.tree[2 * a4], self.tree[2 * a4 + 1])

    def query(self, a1, a2, a3=1, a4=0, a5=None):
        if a5 is None:
            a5 = self.size - 1
        self.propagate(a3, a4, a5)
        if a1 > a5 or a2 < a4:
            return 0
        if a1 <= a4 and a5 <= a2:
            return self.tree[a3]
        v2 = (a4 + a5) // 2
        v3 = self.query(a1, a2, 2 * a3, a4, v2)
        v4 = self.query(a1, a2, 2 * a3 + 1, v2 + 1, a5)
        return max(v3, v4)

class C2:

    def fallingSquares(self, a1):
        v1 = set()
        for v2, v3 in a1:
            v1.add(v2)
            v1.add(v2 + v3 - 1)
        v4 = sorted(v1)
        v5 = len(v4)
        v6 = C1(v5)
        v7 = 0
        v8 = []
        for v2, v3 in a1:
            v9 = v2 + v3 - 1
            v10 = bisect.bisect_left(v4, v2)
            v11 = bisect.bisect_left(v4, v9)
            v12 = v6.query(v10, v11)
            v13 = v12 + v3
            v6.update(v10, v11, v13)
            v7 = max(v7, v13)
            v8.append(v7)
        return v8

class C1:

    def __init__(self, a1, a2):
        self.length = len(a1)
        self.m = a2
        self.t = [None] * (4 * self.length)
        self._build(1, 0, self.length - 1, a1)

    def _build(self, a1, a2, a3, a4):
        if a2 == a3:
            v1 = a4[a2] % self.m
            v2 = [0] * (self.m + 1)
            v2[v1] = 1
            v2[self.m] = v1
            self.t[a1] = v2
            return
        v3 = (a2 + a3) // 2
        self._build(2 * a1, a2, v3, a4)
        self._build(2 * a1 + 1, v3 + 1, a3, a4)
        self.t[a1] = self._merge(self.t[2 * a1], self.t[2 * a1 + 1])

    def _merge(self, a1, a2):
        v1 = a1[:]
        v2 = a1[self.m]
        for v3 in range(self.m):
            v1[v2 * v3 % self.m] += a2[v3]
        v1[self.m] = v2 * a2[self.m] % self.m
        return v1

    def update_pos(self, a1, a2, a3, a4, a5):
        if a2 == a3:
            v1 = a5 % self.m
            v2 = [0] * (self.m + 1)
            v2[v1] = 1
            v2[self.m] = v1
            self.t[a1] = v2
            return
        v3 = (a2 + a3) // 2
        if a4 <= v3:
            self.update_pos(2 * a1, a2, v3, a4, a5)
        else:
            self.update_pos(2 * a1 + 1, v3 + 1, a3, a4, a5)
        self.t[a1] = self._merge(self.t[2 * a1], self.t[2 * a1 + 1])

    def range_query(self, a1, a2, a3, a4, a5):
        if a5 < a2 or a3 < a4:
            return None
        if a4 <= a2 and a3 <= a5:
            return self.t[a1]
        v1 = (a2 + a3) // 2
        v2 = self.range_query(2 * a1, a2, v1, a4, a5)
        v3 = self.range_query(2 * a1 + 1, v1 + 1, a3, a4, a5)
        if v2 is None:
            return v3
        if v3 is None:
            return v2
        return self._merge(v2, v3)

class C2:

    def resultArray(self, a1, a2, a3):
        v1 = len(a1)
        v2 = C1(a1, a2)
        v3 = []
        for v4 in a3:
            v5, v6, v7, v8 = v4
            v2.update_pos(1, 0, v1 - 1, v5, v6)
            v9 = v2.range_query(1, 0, v1 - 1, v7, v1 - 1)
            v3.append(v9[v8])
        return v3

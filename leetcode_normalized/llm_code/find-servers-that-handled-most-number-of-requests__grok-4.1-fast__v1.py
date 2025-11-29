import heapq

class C1:

    def __init__(self, a1):
        self.n = a1
        self.inf = a1 + 10
        self.tree = [self.inf] * (4 * a1)
        self._build(1, 0, a1 - 1)

    def _build(self, a1, a2, a3):
        if a2 == a3:
            self.tree[a1] = a2
            return
        v1 = (a2 + a3) // 2
        self._build(2 * a1, a2, v1)
        self._build(2 * a1 + 1, v1 + 1, a3)
        self.tree[a1] = min(self.tree[2 * a1], self.tree[2 * a1 + 1])

    def update(self, a1, a2):
        self._update(1, 0, self.n - 1, a1, a2)

    def _update(self, a1, a2, a3, a4, a5):
        if a2 == a3:
            self.tree[a1] = a5
            return
        v1 = (a2 + a3) // 2
        if a4 <= v1:
            self._update(2 * a1, a2, v1, a4, a5)
        else:
            self._update(2 * a1 + 1, v1 + 1, a3, a4, a5)
        self.tree[a1] = min(self.tree[2 * a1], self.tree[2 * a1 + 1])

    def query(self, a1, a2):
        return self._query(1, 0, self.n - 1, a1, a2)

    def _query(self, a1, a2, a3, a4, a5):
        if a5 < a2 or a3 < a4:
            return self.inf
        if a4 <= a2 and a3 <= a5:
            return self.tree[a1]
        v1 = (a2 + a3) // 2
        v2 = self._query(2 * a1, a2, v1, a4, a5)
        v3 = self._query(2 * a1 + 1, v1 + 1, a3, a4, a5)
        return min(v2, v3)

class C2:

    def busiestServers(self, a1, a2, a3):
        if a1 == 0:
            return []
        v1 = [0] * a1
        v2 = C1(a1)
        v3 = []
        for v4 in range(len(a2)):
            v5, v6 = (a2[v4], a3[v4])
            v7 = v4 % a1
            while v3 and v3[0][0] <= v5:
                v8, v9 = heapq.heappop(v3)
                v2.update(v9, v9)
            v9 = v2.query(v7, a1 - 1)
            if v9 == v2.inf:
                v9 = v2.query(0, a1 - 1)
            if v9 == v2.inf:
                continue
            v1[v9] += 1
            v2.update(v9, v2.inf)
            heapq.heappush(v3, (v5 + v6, v9))
        v10 = max(v1)
        return [j for v11 in range(a1) if v1[v11] == v10]

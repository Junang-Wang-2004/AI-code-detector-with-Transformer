class C1:

    def __init__(self, a1):
        self.size = a1
        self.data = [0] * (4 * a1)
        self.lazy = [0] * (4 * a1)

    def _push(self, a1, a2, a3):
        if self.lazy[a1]:
            self.data[a1] += self.lazy[a1]
            if a2 != a3:
                self.lazy[2 * a1] += self.lazy[a1]
                self.lazy[2 * a1 + 1] += self.lazy[a1]
            self.lazy[a1] = 0

    def _update(self, a1, a2, a3, a4, a5, a6):
        self._push(a1, a2, a3)
        if a4 > a3 or a5 < a2:
            return
        if a4 <= a2 and a3 <= a5:
            self.lazy[a1] += a6
            self._push(a1, a2, a3)
            return
        v1 = (a2 + a3) // 2
        self._update(2 * a1, a2, v1, a4, a5, a6)
        self._update(2 * a1 + 1, v1 + 1, a3, a4, a5, a6)
        self.data[a1] = max(self.data[2 * a1], self.data[2 * a1 + 1])

    def update_range(self, a1, a2, a3):
        if self.size == 0:
            return
        self._update(1, 0, self.size - 1, a1, a2, a3)

    def _query(self, a1, a2, a3, a4, a5):
        self._push(a1, a2, a3)
        if a4 > a3 or a5 < a2:
            return float('-inf')
        if a4 <= a2 and a3 <= a5:
            return self.data[a1]
        v1 = (a2 + a3) // 2
        return max(self._query(2 * a1, a2, v1, a4, a5), self._query(2 * a1 + 1, v1 + 1, a3, a4, a5))

    def get_max(self):
        if self.size == 0:
            return 0
        return self._query(1, 0, self.size - 1, 0, self.size - 1)

class C2(object):

    def minDayskVariants(self, a1, a2):
        v1 = [[x + y, x - y] for v2, v3 in a1]
        if not v1:
            return 0
        v4 = [p[0] for v5 in v1]
        v6 = [v5[1] for v5 in v1]
        v7 = min(v4)
        v8 = max(v4)
        v9 = min(v6)
        v10 = max(v6)
        v11, v12 = (0, (v8 - v7 + (v10 - v9) + 1) // 2)

        def can_cover(a1):
            v1 = []
            v2 = set()
            for v3, v4 in v1:
                v5 = v3 - a1
                v6 = v3 + a1 + 1
                v7 = v4 - a1
                v8 = v4 + a1
                v1.append((v5, 1, v7, v8))
                v1.append((v6, -1, v7, v8))
                v2.add(v7)
                v2.add(v8)
            v1.sort()
            v9 = sorted(v2)
            v10 = {v3: i for v11, v3 in enumerate(v9)}
            v12 = len(v9)
            v13 = C1(v12)
            for v14, v15, v16, v17 in v1:
                v18 = v10[v16]
                v19 = v10[v17]
                v13.update_range(v18, v19, v15)
                if v13.get_max() >= a2:
                    return True
            return False
        while v11 <= v12:
            v13 = v11 + (v12 - v11) // 2
            if can_cover(v13):
                v12 = v13 - 1
            else:
                v11 = v13 + 1
        return v11

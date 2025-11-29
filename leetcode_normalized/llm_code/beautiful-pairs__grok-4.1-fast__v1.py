class C1:

    def beautifulPair(self, a1, a2):
        v1 = len(a1)
        v2 = 10 ** 20
        v3 = {}
        for v4 in range(v1):
            v5 = (a1[v4], a2[v4])
            if v5 in v3:
                return [v3[v5], v4]
            v3[v5] = v4
        v6 = list(range(v1))
        v6.sort(key=lambda x: a1[x])
        v7 = sorted(set(a2))
        v8 = {y: r for v9, v10 in enumerate(v7)}
        v11 = len(v7)

        class SegTree:

            def __init__(self, a1):
                self.sz = a1
                self.tree = [(-v2, -1)] * (4 * a1)

            def _max(self, a1, a2):
                return max(a1, a2)

            def update(self, a1, a2, a3, a4=1, a5=0, a6=None):
                if a6 is None:
                    a6 = self.sz - 1
                if a5 == a6:
                    if a2 > self.tree[a4][0]:
                        self.tree[a4] = (a2, a3)
                    return
                v2 = (a5 + a6) // 2
                if a1 <= v2:
                    self.update(a1, a2, a3, a4 * 2, a5, v2)
                else:
                    self.update(a1, a2, a3, a4 * 2 + 1, v2 + 1, a6)
                self.tree[a4] = self._max(self.tree[a4 * 2], self.tree[a4 * 2 + 1])

            def query(self, a1, a2, a3=1, a4=0, a5=None):
                if a5 is None:
                    a5 = self.sz - 1
                if a1 > a5 or a2 < a4:
                    return (-v2, -1)
                if a1 <= a4 and a5 <= a2:
                    return self.tree[a3]
                v2 = (a4 + a5) // 2
                v3 = self.query(a1, a2, a3 * 2, a4, v2)
                v4 = self.query(a1, a2, a3 * 2 + 1, v2 + 1, a5)
                return self._max(v3, v4)
        v12 = SegTree(v11)
        v13 = SegTree(v11)

        def get_dist(a1, a2):
            v1 = abs(a1[a1] - a1[a2]) + abs(a2[a1] - a2[a2])
            return (v1, min(a1, a2), max(a1, a2))
        v14 = float('inf')
        v15 = v16 = -1
        for v17 in v6:
            v18 = v8[a2[v17]]
            if v18 > 0:
                v19, v20 = v12.query(0, v18 - 1)
                if v19 > -v2:
                    v21, v22, v23 = get_dist(v17, v20)
                    if v21 < v14:
                        v14 = v21
                        v15, v16 = (v22, v23)
            v24, v20 = v13.query(v18, v11 - 1)
            if v24 > -v2:
                v21, v22, v23 = get_dist(v17, v20)
                if v21 < v14:
                    v14 = v21
                    v15, v16 = (v22, v23)
            v12.update(v18, a1[v17] + a2[v17], v17)
            v13.update(v18, a1[v17] - a2[v17], v17)
        return [v15, v16]

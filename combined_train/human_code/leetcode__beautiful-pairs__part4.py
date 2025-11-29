import itertools

class C1(object):

    def beautifulPair(self, a1, a2):
        """
        """
        v1 = float('inf')

        class SegmentTree(object):

            def __init__(self, a1, a2=lambda _: [-v1, -v1], a3=lambda x, y: y if x is None else x if y is None else max(x, y), a4=lambda x: x):
                self.tree = [None] * (2 * 2 ** (a1 - 1).bit_length())
                self.base = len(self.tree) // 2
                self.query_fn = a3
                self.update_fn = a4
                for v1 in range(self.base, self.base + a1):
                    self.tree[v1] = a2(v1 - self.base)
                for v1 in reversed(range(1, self.base)):
                    self.tree[v1] = a3(self.tree[2 * v1], self.tree[2 * v1 + 1])

            def update(self, a1, a2):
                v1 = self.base + a1
                self.tree[v1] = self.update_fn(a2)
                while v1 > 1:
                    v1 //= 2
                    self.tree[v1] = self.query_fn(self.tree[v1 * 2], self.tree[v1 * 2 + 1])

            def query(self, a1, a2):
                if a1 > a2:
                    return [-v1, -v1]
                a1 += self.base
                a2 += self.base
                v3 = v4 = None
                while a1 <= a2:
                    if a1 & 1:
                        v3 = self.query_fn(v3, self.tree[a1])
                        a1 += 1
                    if a2 & 1 == 0:
                        v4 = self.query_fn(self.tree[a2], v4)
                        a2 -= 1
                    a1 //= 2
                    a2 //= 2
                return self.query_fn(v3, v4)

        def dist(a1, a2):
            if a1 > a2:
                a1, a2 = (a2, a1)
            return [abs(points[a1][0] - points[a2][0]) + abs(points[a1][1] - points[a2][1]), a1, a2]
        v2 = [(i, j) for v3, v4 in zip(a1, a2)]
        v5 = [v1] * 3
        v6 = {}
        for v3 in reversed(range(len(v2))):
            if v2[v3] in v6:
                v5 = [0, (v3, v6[v2[v3]])]
            v6[v2[v3]] = v3
        if v5[0] == 0:
            return v5[1]
        v7 = list(range(len(v2)))
        v7.sort(key=lambda x: v2[x][0])
        v8 = set((y for v9, v10 in v2))
        v11 = {v10: v3 for v3, v10 in enumerate(sorted(v8))}
        v12, v13 = (SegmentTree(len(v11)), SegmentTree(len(v11)))
        for v3 in v7:
            v4 = -v12.query(0, v11[v2[v3][1]] - 1)[1]
            if v4 != v1:
                assert v2[v4][1] < v2[v3][1]
                v5 = min(v5, dist(v3, v4))
            v12.update(v11[v2[v3][1]], [v2[v3][0] + v2[v3][1], -v3])
            v4 = -v13.query(v11[v2[v3][1]], len(v11) - 1)[1]
            if v4 != v1:
                assert v2[v4][1] >= v2[v3][1]
                v5 = min(v5, dist(v3, v4))
            v13.update(v11[v2[v3][1]], [v2[v3][0] - v2[v3][1], -v3])
        return v5[1:]

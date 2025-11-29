class C1:

    def longestBalanced(self, a1):
        v1 = len(a1)

        class SegTree:

            def __init__(self, a1):
                self.size = a1
                self.tmin = [0] * (4 * a1)
                self.tmax = [0] * (4 * a1)
                self.lazy = [0] * (4 * a1)

            def propagate(self, a1, a2, a3):
                if self.lazy[a1]:
                    self.tmin[a1] += self.lazy[a1]
                    self.tmax[a1] += self.lazy[a1]
                    if a2 != a3:
                        self.lazy[2 * a1] += self.lazy[a1]
                        self.lazy[2 * a1 + 1] += self.lazy[a1]
                    self.lazy[a1] = 0

            def update_range(self, a1, a2, a3, a4=1, a5=0, a6=None):
                if a6 is None:
                    a6 = self.size - 1
                self.propagate(a4, a5, a6)
                if a1 > a6 or a2 < a5:
                    return
                if a1 <= a5 and a6 <= a2:
                    self.lazy[a4] += a3
                    self.propagate(a4, a5, a6)
                    return
                v2 = (a5 + a6) // 2
                self.update_range(a1, a2, a3, 2 * a4, a5, v2)
                self.update_range(a1, a2, a3, 2 * a4 + 1, v2 + 1, a6)
                self.tmin[a4] = min(self.tmin[2 * a4], self.tmin[2 * a4 + 1])
                self.tmax[a4] = max(self.tmax[2 * a4], self.tmax[2 * a4 + 1])

            def get_leftmost(self, a1, a2=1, a3=0, a4=None):
                if a4 is None:
                    a4 = self.size - 1
                self.propagate(a2, a3, a4)
                if self.tmin[a2] > a1 or self.tmax[a2] < a1:
                    return float('inf')
                if a3 == a4:
                    return a3 if self.tmin[a2] == a1 else float('inf')
                v2 = (a3 + a4) // 2
                v3 = self.get_leftmost(a1, 2 * a2, a3, v2)
                if v3 != float('inf'):
                    return v3
                return self.get_leftmost(a1, 2 * a2 + 1, v2 + 1, a4)
        v2 = SegTree(v1 + 1)
        v3 = {}
        v4 = 0
        v5 = 0
        for v6 in range(1, v1 + 1):
            v7 = a1[v6 - 1]
            v8 = 1 if v7 & 1 else -1
            if v7 in v3:
                v9 = v3[v7]
                v2.update_range(v9, v1, -v8)
                v4 -= v8
            v4 += v8
            v3[v7] = v6
            v2.update_range(v6, v1, v8)
            v10 = v2.get_leftmost(v4)
            v11 = v6 - v10
            if v11 > v5:
                v5 = v11
        return v5

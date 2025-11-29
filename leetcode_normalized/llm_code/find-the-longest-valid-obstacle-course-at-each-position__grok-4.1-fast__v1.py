class C1:

    def longestObstacleCourseAtEachPosition(self, a1):
        if not a1:
            return []
        v1 = sorted(set(a1))
        v2 = {val: idx + 1 for v3, v4 in enumerate(v1)}
        v5 = len(v1)
        v6 = [0] * (v5 + 2)
        v7 = []
        for v8 in a1:
            v9 = v2[v8]
            v10 = self.prefix_max(v6, v9)
            v11 = v10 + 1
            v7.append(v11)
            self.modify(v6, v9, v11, v5)
        return v7

    def prefix_max(self, a1, a2):
        v1 = 0
        while a2 > 0:
            v1 = max(v1, a1[a2])
            a2 -= a2 & -a2
        return v1

    def modify(self, a1, a2, a3, a4):
        while a2 <= a4:
            a1[a2] = max(a1[a2], a3)
            a2 += a2 & -a2

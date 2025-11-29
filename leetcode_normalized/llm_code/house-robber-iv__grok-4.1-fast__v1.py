class C1:

    def minCapability(self, a1, a2):
        v1 = sorted({v for v2 in a1})
        v3, v4 = (0, len(v1) - 1)
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if self._feasible(a1, a2, v1[v5]):
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        return v1[v3]

    def _feasible(self, a1, a2, a3):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            if a1[v2] <= a3:
                v1 += 1
                v2 += 2
            else:
                v2 += 1
        return v1 >= a2

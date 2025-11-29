class C1:

    def findMinimumTime(self, a1):
        v1 = len(a1)
        v2 = sorted(a1, reverse=True)
        v3 = 0
        for v4 in range(v1):
            v5 = v1 - v4
            v3 += (v2[v4] + v5 - 1) // v5
        return v3

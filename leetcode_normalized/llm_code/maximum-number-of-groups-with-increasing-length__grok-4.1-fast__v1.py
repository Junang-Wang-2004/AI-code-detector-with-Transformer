class C1:

    def maxIncreasingGroups(self, a1):
        v1 = len(a1)
        v2 = sorted((min(limit, v1) for v3 in a1))
        v4 = 0
        v5 = 0
        for v6 in v2:
            v5 += v6
            while v5 >= v4 + 1:
                v5 -= v4 + 1
                v4 += 1
        return v4

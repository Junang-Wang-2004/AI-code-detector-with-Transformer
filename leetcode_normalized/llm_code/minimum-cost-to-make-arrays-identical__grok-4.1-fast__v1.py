class C1:

    def minCost(self, a1, a2, a3):
        v1 = len(a1)
        v2 = 0
        for v3 in range(v1):
            v2 += abs(a1[v3] - a2[v3])
        a1.sort()
        a2.sort()
        v4 = 0
        for v3 in range(v1):
            v4 += abs(a1[v3] - a2[v3])
        return min(v2, a3 + v4)

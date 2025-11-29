class C1:

    def minCost(self, a1):
        if not a1:
            return 0
        v1, v2, v3 = a1[0]
        for v4 in a1[1:]:
            v5 = v4[0] + min(v2, v3)
            v6 = v4[1] + min(v1, v3)
            v7 = v4[2] + min(v1, v2)
            v1, v2, v3 = (v5, v6, v7)
        return min(v1, v2, v3)

class C1:

    def maxProfit(self, a1):
        if not a1:
            return 0
        v1 = -a1[0]
        v2 = 0
        v3 = 0
        for v4 in a1[1:]:
            v5 = max(v1, v3 - v4)
            v6 = v1 + v4
            v7 = max(v3, v2)
            v1 = v5
            v2 = v6
            v3 = v7
        return max(v3, v2)

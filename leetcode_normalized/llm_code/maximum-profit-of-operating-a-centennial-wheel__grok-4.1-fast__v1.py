class C1:

    def minOperationsMaxProfit(self, a1, a2, a3):
        v1 = 0
        v2 = -1
        v3 = 0
        v4 = 0
        v5 = 0
        for v6 in a1:
            v4 += v6
            v5 += 1
            v7 = min(4, v4)
            v4 -= v7
            v3 += v7 * a2 - a3
            if v3 > v1:
                v1 = v3
                v2 = v5
        while v4 > 0:
            v5 += 1
            v7 = min(4, v4)
            v4 -= v7
            v3 += v7 * a2 - a3
            if v3 > v1:
                v1 = v3
                v2 = v5
        return v2

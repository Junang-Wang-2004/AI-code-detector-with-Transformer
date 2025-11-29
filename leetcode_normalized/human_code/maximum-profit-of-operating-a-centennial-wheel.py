class C1(object):

    def minOperationsMaxProfit(self, a1, a2, a3):
        """
        """
        v1 = -1
        v2 = v3 = v4 = v5 = 0
        v6 = 1
        while v2 < len(a1) or v5 > 0:
            if v2 < len(a1):
                v5 += a1[v2]
                v2 += 1
            v7 = min(v5, 4)
            v5 -= v7
            v4 += v7 * a2 - a3
            if v4 > v3:
                v3 = v4
                v1 = v6
            v6 += 1
        return v1

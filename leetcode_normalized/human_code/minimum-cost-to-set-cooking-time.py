class C1(object):

    def minCostSetTime(self, a1, a2, a3, a4):
        """
        """

        def cost(a1, a2):
            if not (0 <= a1 <= 99 and a2 <= 99):
                return float('inf')
            v1 = 0
            v2 = a1
            for v3 in map(int, list(str(a1 * 100 + a2))):
                v1 += (a2 if v3 != v2 else 0) + a3
                v2 = v3
            return v1
        v1, v2 = divmod(a4, 60)
        return min(cost(v1, v2), cost(v1 - 1, v2 + 60))

class C1(object):

    def maxProfit(self, a1):
        """
        """

        def maxAtMostKPairsProfit(a1, a2):
            v1 = [float('-inf') for v2 in range(a2 + 1)]
            v3 = [0 for v2 in range(a2 + 1)]
            for v4 in range(len(a1)):
                for v5 in range(1, a2 + 1):
                    v1[v5] = max(v1[v5], v3[v5 - 1] - a1[v4])
                    v3[v5] = max(v3[v5], v1[v5] + a1[v4])
            return v3[a2]
        return maxAtMostKPairsProfit(a1, 2)

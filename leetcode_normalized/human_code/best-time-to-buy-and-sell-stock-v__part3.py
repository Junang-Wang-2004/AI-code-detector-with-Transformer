class C1(object):

    def maximumProfit(self, a1, a2):
        """
        """
        v1 = [float('-inf')] * a2
        v2 = [float('-inf')] * a2
        v3 = [float('-inf')] * (a2 + 1)
        v3[0] = 0
        for v4 in a1:
            for v5 in reversed(range(a2)):
                v3[v5 + 1] = max(v3[v5 + 1], v1[v5] + v4, v2[v5] - v4)
                v1[v5] = max(v1[v5], v3[v5] - v4)
                v2[v5] = max(v2[v5], v3[v5] + v4)
        return max(v3)

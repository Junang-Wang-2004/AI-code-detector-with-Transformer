class C1(object):

    def maxProfit(self, a1):
        """
        """
        v1, v2 = (float('-inf'), float('-inf'))
        v3, v4 = (0, 0)
        for v5 in a1:
            v1 = max(v1, -v5)
            v3 = max(v3, v1 + v5)
            v2 = max(v2, v3 - v5)
            v4 = max(v4, v2 + v5)
        return v4

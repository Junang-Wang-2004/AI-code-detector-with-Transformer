class C1(object):

    def maxProfit(self, a1, a2):
        """
        """
        v1, v2 = (0, -a1[0])
        for v3 in range(1, len(a1)):
            v1 = max(v1, v2 + a1[v3] - a2)
            v2 = max(v2, v1 - a1[v3])
        return v1

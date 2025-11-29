class C1(object):

    def minCost(self, a1):
        """
        """
        if not a1:
            return 0
        v1 = len(a1)
        for v2 in range(1, v1):
            a1[v2][0] += min(a1[v2 - 1][1], a1[v2 - 1][2])
            a1[v2][1] += min(a1[v2 - 1][0], a1[v2 - 1][2])
            a1[v2][2] += min(a1[v2 - 1][0], a1[v2 - 1][1])
        return min(a1[v1 - 1])

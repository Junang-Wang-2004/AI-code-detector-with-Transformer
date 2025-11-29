class C1(object):

    def minCostToMoveChips(self, a1):
        """
        """
        v1 = [0] * 2
        for v2 in a1:
            v1[v2 % 2] += 1
        return min(v1)

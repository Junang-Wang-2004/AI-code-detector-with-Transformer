class C1(object):

    def minCuttingCost(self, a1, a2, a3):
        """
        """
        return a3 * max(a1 - a3, a2 - a3, 0)

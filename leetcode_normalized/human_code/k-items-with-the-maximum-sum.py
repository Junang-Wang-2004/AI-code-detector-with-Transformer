class C1(object):

    def kItemsWithMaximumSum(self, a1, a2, a3, a4):
        """
        """
        return min(a1, a4) - max(a4 - a1 - a2, 0)

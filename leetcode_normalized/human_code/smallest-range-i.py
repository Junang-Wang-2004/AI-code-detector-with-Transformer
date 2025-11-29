class C1(object):

    def smallestRangeI(self, a1, a2):
        """
        """
        return max(0, max(a1) - min(a1) - 2 * a2)

class C1(object):

    def subsetXORSum(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            v1 |= v2
        return v1 * 2 ** (len(a1) - 1)

class C1(object):

    def minMoves(self, a1):
        """
        """
        return max(a1) * len(a1) - sum(a1)

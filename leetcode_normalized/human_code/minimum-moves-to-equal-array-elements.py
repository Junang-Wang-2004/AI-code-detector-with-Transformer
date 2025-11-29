class C1(object):

    def minMoves(self, a1):
        """
        """
        return sum(a1) - len(a1) * min(a1)

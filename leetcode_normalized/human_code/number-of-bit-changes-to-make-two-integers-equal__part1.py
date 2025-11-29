class C1(object):

    def minChanges(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        return popcount(a1 ^ a2) if a1 & a2 == a2 else -1

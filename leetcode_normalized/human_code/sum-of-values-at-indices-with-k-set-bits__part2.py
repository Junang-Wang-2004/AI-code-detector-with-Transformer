class C1(object):

    def sumIndicesWithKSetBits(self, a1, a2):
        """
        """

        def popcount(a1):
            return bin(a1)[1:].count('1')
        return sum((x for v1, v2 in enumerate(a1) if popcount(v1) == a2))

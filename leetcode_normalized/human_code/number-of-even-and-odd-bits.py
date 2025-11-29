class C1(object):

    def evenOddBit(self, a1):
        """
        """

        def popcount(a1):
            return bin(a1)[2:].count('1')
        return [popcount(a1 & 341), popcount(a1 & 682)]

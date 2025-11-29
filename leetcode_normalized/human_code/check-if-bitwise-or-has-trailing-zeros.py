class C1(object):

    def hasTrailingZeros(self, a1):
        """
        """
        return sum((x % 2 == 0 for v1 in a1)) >= 2

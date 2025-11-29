class C1(object):

    def minimumOneBitOperations(self, a1):
        """
        """
        v1 = 0
        while a1:
            v1 = -v1 - (a1 ^ a1 - 1)
            a1 &= a1 - 1
        return abs(v1)

class C1(object):

    def isPowerOfFour(self, a1):
        """
        """
        return a1 > 0 and a1 & a1 - 1 == 0 and (a1 & 1431655765 == a1)

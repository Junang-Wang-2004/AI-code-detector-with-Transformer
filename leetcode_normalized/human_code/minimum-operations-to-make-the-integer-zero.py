class C1(object):

    def makeTheIntegerZero(self, a1, a2):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        for v1 in range(1, 60 + 1):
            if a1 - v1 * a2 < 0:
                break
            if popcount(a1 - v1 * a2) <= v1 <= a1 - v1 * a2:
                return v1
        return -1

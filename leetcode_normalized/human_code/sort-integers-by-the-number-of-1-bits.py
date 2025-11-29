class C1(object):

    def sortByBits(self, a1):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        a1.sort(key=lambda x: (popcount(x), x))
        return a1

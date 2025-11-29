class C1(object):

    def countPrimeSetBits(self, a1, a2):
        """
        """

        def bitCount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        v1 = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum((bitCount(i) in v1 for v2 in range(a1, a2 + 1)))

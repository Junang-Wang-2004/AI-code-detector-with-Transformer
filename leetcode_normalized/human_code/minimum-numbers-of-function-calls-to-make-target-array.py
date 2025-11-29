class C1(object):

    def minOperations(self, a1):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        v1, v2 = (0, 1)
        for v3 in a1:
            v1 += popcount(v3)
            v2 = max(v2, v3.bit_length())
        return v1 + (v2 - 1)

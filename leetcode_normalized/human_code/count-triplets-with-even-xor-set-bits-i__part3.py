class C1(object):

    def tripletCount(self, a1, a2, a3):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        return sum((popcount(x ^ y ^ z) % 2 == 0 for v1 in a1 for v2 in a2 for v3 in a3))

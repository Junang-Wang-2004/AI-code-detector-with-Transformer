class C1(object):

    def numberOfSets(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def nCr(a1, a2):
            if a1 - a2 < a2:
                return nCr(a1, a1 - a2)
            v1 = 1
            for v2 in range(1, a2 + 1):
                v1 *= a1 - v2 + 1
                v1 //= v2
            return v1
        return nCr(a1 + a2 - 1, 2 * a2) % v1

class C1(object):

    def uniquePaths(self, a1, a2):
        """
        """

        def nCr(a1, a2):
            if a1 - a2 < a2:
                a2 = a1 - a2
            v2 = 1
            for v3 in range(1, a2 + 1):
                v2 *= a1 - v3 + 1
                v2 //= v3
            return v2
        return nCr(a1 - 1 + (a2 - 1), a2 - 1)

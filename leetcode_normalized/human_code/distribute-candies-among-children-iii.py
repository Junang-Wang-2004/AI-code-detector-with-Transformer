class C1(object):

    def distributeCandies(self, a1, a2):
        """
        """

        def nCr(a1, a2):
            if not 0 <= a2 <= a1:
                return 0
            if a1 - a2 < a2:
                a2 = a1 - a2
            v2 = 1
            for v3 in range(1, a2 + 1):
                v2 *= a1 - v3 + 1
                v2 //= v3
            return v2

        def nHr(a1, a2):
            return nCr(a1 + (a2 - 1), a2 - 1)
        v1 = 3
        return sum(((-1 if r % 2 else 1) * nCr(v1, r) * nHr(a1 - r * (a2 + 1), v1) for v2 in range(v1 + 1)))

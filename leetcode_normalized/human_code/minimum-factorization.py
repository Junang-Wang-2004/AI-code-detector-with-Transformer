class C1(object):

    def smallestFactorization(self, a1):
        """
        """
        if a1 < 2:
            return a1
        v1, v2 = (0, 1)
        for v3 in reversed(range(2, 10)):
            while a1 % v3 == 0:
                a1 /= v3
                v1 = v2 * v3 + v1
                v2 *= 10
        return v1 if a1 == 1 and v1 < 2 ** 31 else 0

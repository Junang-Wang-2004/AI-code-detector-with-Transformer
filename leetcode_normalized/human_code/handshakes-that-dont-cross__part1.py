class C1(object):

    def numberOfWays(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def inv(a1, a2):
            return pow(a1, a2 - 2, a2)

        def nCr(a1, a2, a3):
            if a1 - a2 < a2:
                return nCr(a1, a1 - a2, a3)
            v1 = 1
            for v2 in range(1, a2 + 1):
                v1 = v1 * (a1 - a2 + v2) * inv(v2, a3) % a3
            return v1
        v2 = a1 // 2
        return nCr(2 * v2, v2, v1) * inv(v2 + 1, v1) % v1

class C1(object):

    def digitsCount(self, a1, a2, a3):
        """
        """

        def digitsCount(a1, a2):
            v1, v2 = (1, 0)
            while a1 >= v1:
                v2 += a1 // (10 * v1) * v1 + min(v1, max(a1 % (10 * v1) - a2 * v1 + 1, 0))
                if a2 == 0:
                    v2 -= v1
                v1 *= 10
            return v2 + 1
        return digitsCount(a3, a1) - digitsCount(a2 - 1, a1)

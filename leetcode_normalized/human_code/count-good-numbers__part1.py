class C1(object):

    def countGoodNumbers(self, a1):
        """
        """

        def powmod(a1, a2, a3):
            a1 %= a3
            v2 = 1
            while a2:
                if a2 & 1:
                    v2 = v2 * a1 % a3
                a1 = a1 * a1 % a3
                a2 >>= 1
            return v2
        v1 = 10 ** 9 + 7
        return powmod(5, (a1 + 1) // 2 % (v1 - 1), v1) * powmod(4, a1 // 2 % (v1 - 1), v1) % v1

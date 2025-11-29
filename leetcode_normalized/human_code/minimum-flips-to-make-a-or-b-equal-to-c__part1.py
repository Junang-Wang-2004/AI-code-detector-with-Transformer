class C1(object):

    def minFlips(self, a1, a2, a3):
        """
        """

        def number_of_1_bits(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1
        return number_of_1_bits((a1 | a2) ^ a3) + number_of_1_bits(a1 & a2 & ~a3)

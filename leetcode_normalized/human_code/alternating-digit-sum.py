class C1(object):

    def alternateDigitSum(self, a1):
        """
        """
        v1 = 0
        v2 = 1
        while a1:
            v2 *= -1
            v1 += v2 * (a1 % 10)
            a1 //= 10
        return v2 * v1

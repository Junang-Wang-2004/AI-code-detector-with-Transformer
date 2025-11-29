class C1(object):

    def countNumbersWithUniqueDigits(self, a1):
        """
        """
        if a1 == 0:
            return 1
        v1 = v2 = 1
        for v3 in range(a1 - 1):
            v2 *= 9 - v3
            v1 += v2
        return 1 + 9 * v1

class C1(object):

    def findNthDigit(self, a1):
        """
        """
        v1 = 1
        while a1 > v1 * 9 * 10 ** (v1 - 1):
            a1 -= v1 * 9 * 10 ** (v1 - 1)
            v1 += 1
        v3 = 10 ** (v1 - 1) + (a1 - 1) / v1
        v4 = v3 / 10 ** (v1 - 1 - (a1 - 1) % v1)
        v4 %= 10
        return v4

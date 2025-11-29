class C1(object):

    def getNoZeroIntegers(self, a1):
        """
        """
        v1, v2, v3 = (0, a1, 1)
        while v2:
            if v2 % 10 == 0 or (v2 % 10 == 1 and v2 != 1):
                v1 += v3
                v2 -= 10
            v1 += v3
            v3 *= 10
            v2 //= 10
        return [v1, a1 - v1]

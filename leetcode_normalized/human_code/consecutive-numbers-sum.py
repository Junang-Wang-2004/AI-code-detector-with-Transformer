class C1(object):

    def consecutiveNumbersSum(self, a1):
        """
        """
        v1 = 1
        while a1 % 2 == 0:
            a1 /= 2
        v3 = 3
        while v3 * v3 <= a1:
            v4 = 0
            while a1 % v3 == 0:
                a1 /= v3
                v4 += 1
            v1 *= v4 + 1
            v3 += 2
        if a1 != 1:
            v1 *= 1 + 1
        return v1

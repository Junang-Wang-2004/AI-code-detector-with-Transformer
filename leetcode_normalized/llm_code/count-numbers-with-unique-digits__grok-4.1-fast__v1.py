class C1(object):

    def countNumbersWithUniqueDigits(self, a1):
        if a1 == 0:
            return 1
        v1 = 1
        v2 = 1
        v1 += 9 * v2
        for v3 in range(2, a1 + 1):
            v2 *= 11 - v3
            v1 += 9 * v2
        return v1

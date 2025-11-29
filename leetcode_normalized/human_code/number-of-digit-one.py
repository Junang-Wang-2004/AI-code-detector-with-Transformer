class C1(object):

    def countDigitOne(self, a1):
        """
        """
        v1 = 1
        v2 = int(v1 == 0)
        v3 = v2
        v4 = 1
        while a1 >= v4:
            v3 += (a1 // (10 * v4) - v2) * v4 + min(v4, max(a1 % (10 * v4) - v1 * v4 + 1, 0))
            v4 *= 10
        return v3

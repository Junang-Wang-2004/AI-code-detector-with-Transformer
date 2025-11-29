class C1(object):

    def reachNumber(self, a1):
        """
        """
        a1 = abs(a1)
        v2 = 0
        while a1 > 0:
            v2 += 1
            a1 -= v2
        return v2 if a1 % 2 == 0 else v2 + 1 + v2 % 2

class C1(object):

    def checkPerfectNumber(self, a1):
        """
        """
        if a1 <= 0:
            return False
        v1 = int(a1 ** 0.5)
        v2 = sum((i + a1 // i for v3 in range(1, v1 + 1) if a1 % v3 == 0))
        if v1 ** 2 == a1:
            v2 -= v1
        return v2 - a1 == a1

class C1(object):

    def sumOfPower(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = v3 = 0
        for v4 in a1:
            v2 = (v2 + v4 ** 2 * (v3 + v4)) % v1
            v3 = (v3 + (v3 + v4)) % v1
        return v2

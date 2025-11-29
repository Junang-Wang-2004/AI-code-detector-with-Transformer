class C1(object):

    def checkDivisibility(self, a1):
        """
        """
        v1 = a1
        v2, v3 = (0, 1)
        while v1:
            v1, v4 = divmod(v1, 10)
            v2 += v4
            v3 *= v4
        return a1 % (v2 + v3) == 0

class C1(object):

    def newInteger(self, a1):
        """
        """
        v1, v2 = (0, 1)
        while a1 > 0:
            v1 += a1 % 9 * v2
            a1 /= 9
            v2 *= 10
        return v1

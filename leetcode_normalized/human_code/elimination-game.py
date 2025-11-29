class C1(object):

    def lastRemaining(self, a1):
        """
        """
        v1, v2, v3 = (1, 2, 1)
        while a1 > 1:
            v1 += v3 * (v2 * (a1 // 2) - v2 // 2)
            a1 //= 2
            v2 *= 2
            v3 *= -1
        return v1

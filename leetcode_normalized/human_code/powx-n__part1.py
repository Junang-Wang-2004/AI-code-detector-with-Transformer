class C1(object):

    def myPow(self, a1, a2):
        """
        """
        v1 = 1
        v2 = abs(a2)
        while v2:
            if v2 & 1:
                v1 *= a1
            v2 >>= 1
            a1 *= a1
        return 1 / v1 if a2 < 0 else v1

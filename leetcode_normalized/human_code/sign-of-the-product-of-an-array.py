class C1(object):

    def arraySign(self, a1):
        """
        """
        v1 = 0
        for v2 in a1:
            if not v2:
                return 0
            if v2 < 0:
                v1 ^= 1
        return -1 if v1 else 1

class C1(object):

    def mySqrt(self, a1):
        """
        """
        if a1 < 2:
            return a1
        v1, v2 = (1, a1 // 2)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if v3 > a1 / v3:
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1 - 1

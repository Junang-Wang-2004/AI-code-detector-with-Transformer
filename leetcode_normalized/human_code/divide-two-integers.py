class C1(object):

    def divide(self, a1, a2):
        """
        """
        v1, v2, v3 = (0, abs(a1), abs(a2))
        while v2 >= v3:
            v4 = v3
            v5 = 0
            while v2 >= v4:
                v2 -= v4
                v1 += 1 << v5
                v4 <<= 1
                v5 += 1
        if a1 > 0 and a2 < 0 or (a1 < 0 and a2 > 0):
            return -v1
        else:
            return v1

    def divide2(self, a1, a2):
        """
        """
        v1 = (a1 < 0) is (a2 < 0)
        a1, a2 = (abs(a1), abs(a2))
        v4 = 0
        while a1 >= a2:
            v5, v6 = (a2, 1)
            while a1 >= v5:
                a1 -= v5
                v4 += v6
                v6 <<= 1
                v5 <<= 1
        if not v1:
            v4 = -v4
        return min(max(-2147483648, v4), 2147483647)

class C1(object):

    def isPerfectSquare(self, a1):
        """
        """
        v1, v2 = (1, a1)
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if v3 >= a1 / v3:
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1 == a1 / v1 and a1 % v1 == 0

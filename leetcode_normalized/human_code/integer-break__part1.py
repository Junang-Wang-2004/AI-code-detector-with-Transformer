class C1(object):

    def integerBreak(self, a1):
        """
        """
        if a1 < 4:
            return a1 - 1
        v1 = 0
        if a1 % 3 == 0:
            v1 = 3 ** (a1 // 3)
        elif a1 % 3 == 2:
            v1 = 3 ** (a1 // 3) * 2
        else:
            v1 = 3 ** (a1 // 3 - 1) * 4
        return v1

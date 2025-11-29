class C1(object):

    def canAliceWin(self, a1):
        """
        """
        v1 = 10
        v2 = int((2 * v1 + 1 - ((2 * v1 + 1) ** 2 - 8 * a1) ** 0.5) / 2)
        return v2 % 2 == 1

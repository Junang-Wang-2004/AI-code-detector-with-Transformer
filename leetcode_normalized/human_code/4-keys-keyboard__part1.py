class C1(object):

    def maxA(self, a1):
        """
        """
        if a1 < 7:
            return a1
        if a1 == 10:
            return 20
        v1 = a1 // 5 + 1
        v2 = 5 * v1 - a1 - 1
        v3 = v1 - v2
        return 3 ** v2 * 4 ** v3

class C1(object):

    def canAliceWin(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 < 10:
                v1 += v3
            else:
                v2 += v3
        return v1 != v2

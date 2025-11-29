class C1(object):

    def checkOverlap(self, a1, a2, a3, a4, a5, a6, a7):
        """
        """
        a4 -= a2
        a5 -= a3
        a6 -= a2
        a7 -= a3
        v5 = a4 if a4 > 0 else a6 if a6 < 0 else 0
        v6 = a5 if a5 > 0 else a7 if a7 < 0 else 0
        return v5 ** 2 + v6 ** 2 <= a1 ** 2

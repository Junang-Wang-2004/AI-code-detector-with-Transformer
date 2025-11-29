class C1(object):

    def checkOverlap(self, a1, a2, a3, a4, a5, a6, a7):
        """
        """
        a4 -= a2
        a5 -= a3
        a6 -= a2
        a7 -= a3
        v5 = min(abs(a4), abs(a6)) if a4 * a6 > 0 else 0
        v6 = min(abs(a5), abs(a7)) if a5 * a7 > 0 else 0
        return v5 ** 2 + v6 ** 2 <= a1 ** 2

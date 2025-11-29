class C1(object):

    def angleClock(self, a1, a2):
        """
        """
        v1 = (a1 % 12 * 60.0 + a2) / 720.0
        v2 = a2 / 60.0
        v3 = abs(v1 - v2)
        return min(v3, 1.0 - v3) * 360.0

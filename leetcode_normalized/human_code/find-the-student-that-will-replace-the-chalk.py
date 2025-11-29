class C1(object):

    def chalkReplacer(self, a1, a2):
        """
        """
        a2 %= sum(a1)
        for v2, v3 in enumerate(a1):
            if a2 < v3:
                return v2
            a2 -= v3
        return -1

class C1(object):

    def stringShift(self, a1, a2):
        """
        """
        v1 = 0
        for v2, v3 in a2:
            if not v2:
                v1 += v3
            else:
                v1 -= v3
        v1 %= len(a1)
        return a1[v1:] + a1[:v1]

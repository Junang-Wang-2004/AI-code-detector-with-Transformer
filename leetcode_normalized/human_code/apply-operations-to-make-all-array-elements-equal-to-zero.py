class C1(object):

    def checkArray(self, a1, a2):
        """
        """
        v1 = 0
        for v2, v3 in enumerate(a1):
            if v3 - v1 < 0:
                return False
            a1[v2] -= v1
            v1 += a1[v2]
            if v2 - (a2 - 1) >= 0:
                v1 -= a1[v2 - (a2 - 1)]
        return v1 == 0

class C1(object):

    def countGoodRectangles(self, a1):
        """
        """
        v1 = v2 = 0
        for v3, v4 in a1:
            v5 = min(v3, v4)
            if v5 > v2:
                v1, v2 = (1, v5)
            elif v5 == v2:
                v1 += 1
        return v1

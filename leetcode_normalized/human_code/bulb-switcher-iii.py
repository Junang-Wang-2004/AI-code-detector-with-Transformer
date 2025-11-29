class C1(object):

    def numTimesAllBlue(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3, v4 in enumerate(a1, 1):
            v2 = max(v2, v4)
            v1 += v2 == v3
        return v1

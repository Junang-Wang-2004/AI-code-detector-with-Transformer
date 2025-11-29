class C1(object):

    def returnToBoundaryCount(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            v2 += v3
            if v2 == 0:
                v1 += 1
        return v1

class C1(object):

    def maxAbsoluteSum(self, a1):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in a1:
            v1 += v4
            v2 = max(v2, v1)
            v3 = min(v3, v1)
        return v2 - v3

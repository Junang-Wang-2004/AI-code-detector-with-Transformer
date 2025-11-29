class C1(object):

    def findMaximumScore(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            v1 += v2
            v2 = max(v2, v3)
        return v1

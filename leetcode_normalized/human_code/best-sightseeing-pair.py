class C1(object):

    def maxScoreSightseeingPair(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in a1:
            v1 = max(v1, v2 + v3)
            v2 = max(v2, v3) - 1
        return v1

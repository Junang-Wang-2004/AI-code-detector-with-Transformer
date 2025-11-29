class C1(object):

    def maximumDifference(self, a1):
        """
        """
        v1, v2 = (0, float('inf'))
        for v3 in a1:
            v1 = max(v1, v3 - v2)
            v2 = min(v2, v3)
        return v1 if v1 else -1

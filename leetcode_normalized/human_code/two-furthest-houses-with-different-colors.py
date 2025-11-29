class C1(object):

    def maxDistance(self, a1):
        """
        """
        v1 = 0
        for v2, v3 in enumerate(a1):
            if v3 != a1[0]:
                v1 = max(v1, v2)
            if v3 != a1[-1]:
                v1 = max(v1, len(a1) - 1 - v2)
        return v1

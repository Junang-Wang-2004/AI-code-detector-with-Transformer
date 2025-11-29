class C1(object):

    def maxDistance(self, a1):
        """
        """
        v1, v2, v3 = (0, a1[0][0], a1[0][-1])
        for v4 in range(1, len(a1)):
            v1 = max(v1, max(v3 - a1[v4][0], a1[v4][-1] - v2))
            v2 = min(v2, a1[v4][0])
            v3 = max(v3, a1[v4][-1])
        return v1

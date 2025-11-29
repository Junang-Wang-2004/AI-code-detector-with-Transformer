class C1(object):

    def maxScore(self, a1):
        """
        """
        v1 = [0] * len(a1)
        for v2 in range(1, len(a1)):
            for v3 in range(v2):
                v1[v2] = max(v1[v2], v1[v3] + (v2 - v3) * a1[v2])
        return v1[-1]

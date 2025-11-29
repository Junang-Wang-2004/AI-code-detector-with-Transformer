class C1(object):

    def maxScore(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in reversed(range(1, len(a1))):
            v2 = max(v2, a1[v3])
            v1 += v2
        return v1

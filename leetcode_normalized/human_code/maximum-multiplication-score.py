class C1(object):

    def maxScore(self, a1, a2):
        """
        """
        v1 = [float('-inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2 in a2:
            for v3 in reversed(range(1, len(v1))):
                v1[v3] = max(v1[v3], v1[v3 - 1] + v2 * a1[v3 - 1])
        return v1[-1]

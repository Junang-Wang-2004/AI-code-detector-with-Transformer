class C1(object):

    def maxSumTwoNoOverlap(self, a1, a2, a3):
        """
        """
        for v1 in range(1, len(a1)):
            a1[v1] += a1[v1 - 1]
        v2, v3, v4 = (a1[a2 + a3 - 1], a1[a2 - 1], a1[a3 - 1])
        for v1 in range(a2 + a3, len(a1)):
            v3 = max(v3, a1[v1 - a3] - a1[v1 - a2 - a3])
            v4 = max(v4, a1[v1 - a2] - a1[v1 - a2 - a3])
            v2 = max(v2, v3 + a1[v1] - a1[v1 - a3], v4 + a1[v1] - a1[v1 - a2])
        return v2

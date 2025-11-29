class C1(object):

    def maxNonDecreasingLength(self, a1, a2):
        """
        """
        v1 = 1
        v2 = [1] * 2
        for v3 in range(len(a1) - 1):
            v2 = [max(v2[0] + 1 if a1[v3] <= a1[v3 + 1] else 1, v2[1] + 1 if a2[v3] <= a1[v3 + 1] else 1), max(v2[0] + 1 if a1[v3] <= a2[v3 + 1] else 1, v2[1] + 1 if a2[v3] <= a2[v3 + 1] else 1)]
            v1 = max(v1, max(v2))
        return v1

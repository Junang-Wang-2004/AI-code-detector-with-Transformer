class C1(object):

    def longestMonotonicSubarray(self, a1):
        """
        """
        v1 = v2 = v3 = 1
        for v4 in range(1, len(a1)):
            v2 = v2 + 1 if a1[v4 - 1] < a1[v4] else 1
            v3 = v3 + 1 if a1[v4 - 1] > a1[v4] else 1
            v1 = max(v1, v2, v3)
        return v1

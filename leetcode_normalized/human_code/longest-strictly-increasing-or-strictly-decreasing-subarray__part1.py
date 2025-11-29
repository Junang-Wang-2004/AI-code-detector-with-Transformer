class C1(object):

    def longestMonotonicSubarray(self, a1):
        """
        """
        v1 = v2 = 1 if len(a1) == 1 or cmp(a1[0], a1[1]) == 0 else 2
        for v3 in range(2, len(a1)):
            v2 = 1 if cmp(a1[v3 - 1], a1[v3]) == 0 else v2 + 1 if cmp(a1[v3 - 2], a1[v3 - 1]) == cmp(a1[v3 - 1], a1[v3]) else 2
            v1 = max(v1, v2)
        return v1

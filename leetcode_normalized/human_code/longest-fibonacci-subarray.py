class C1(object):

    def longestSubarray(self, a1):
        """
        """
        v1 = v2 = 2
        for v3 in range(2, len(a1)):
            if a1[v3] != a1[v3 - 1] + a1[v3 - 2]:
                v2 = 2
                continue
            v2 += 1
            v1 = max(v1, v2)
        return v1

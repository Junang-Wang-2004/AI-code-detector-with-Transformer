class C1(object):

    def longestSubarray(self, a1):
        """
        """
        v1 = max(a1)
        v2, v3 = (1, 0)
        for v4 in a1:
            if v4 == v1:
                v3 += 1
                v2 = max(v2, v3)
            else:
                v3 = 0
        return v2

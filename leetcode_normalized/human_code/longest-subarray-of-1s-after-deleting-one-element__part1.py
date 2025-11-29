class C1(object):

    def longestSubarray(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            v1 += a1[v3] == 0
            if v1 >= 2:
                v1 -= a1[v2] == 0
                v2 += 1
        return v3 - v2 + 1 - 1

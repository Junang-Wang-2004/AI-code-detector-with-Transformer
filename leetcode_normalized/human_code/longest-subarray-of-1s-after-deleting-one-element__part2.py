class C1(object):

    def longestSubarray(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, 0)
        for v4 in range(len(a1)):
            v2 += a1[v4] == 0
            while v2 >= 2:
                v2 -= a1[v3] == 0
                v3 += 1
            v1 = max(v1, v4 - v3 + 1)
        return v1 - 1

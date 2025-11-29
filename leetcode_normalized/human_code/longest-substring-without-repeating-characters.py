class C1(object):

    def lengthOfLongestSubstring(self, a1):
        """
        """
        v1, v2 = (0, 0)
        v3 = {}
        for v4 in range(len(a1)):
            if a1[v4] in v3:
                v2 = max(v2, v3[a1[v4]] + 1)
            v3[a1[v4]] = v4
            v1 = max(v1, v4 - v2 + 1)
        return v1

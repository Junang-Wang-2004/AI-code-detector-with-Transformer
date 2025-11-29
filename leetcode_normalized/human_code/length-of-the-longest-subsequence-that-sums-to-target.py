class C1(object):

    def lengthOfLongestSubsequence(self, a1, a2):
        """
        """
        v1 = [-1] * (a2 + 1)
        v1[0] = 0
        for v2 in a1:
            for v3 in reversed(range(v2, len(v1))):
                if v1[v3 - v2] != -1:
                    v1[v3] = max(v1[v3], v1[v3 - v2] + 1)
        return v1[-1]

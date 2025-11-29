class C1(object):

    def countPalindromicSubsequence(self, a1):
        """
        """
        v1, v2 = ([len(a1)] * 26, [-1] * 26)
        for v3, v4 in enumerate(a1):
            v1[ord(v4) - ord('a')] = min(v1[ord(v4) - ord('a')], v3)
            v2[ord(v4) - ord('a')] = max(v2[ord(v4) - ord('a')], v3)
        return sum((len(set((a1[v3] for v3 in range(v1[v4] + 1, v2[v4])))) for v4 in range(26)))

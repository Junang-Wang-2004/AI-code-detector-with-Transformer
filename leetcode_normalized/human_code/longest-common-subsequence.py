class C1(object):

    def longestCommonSubsequence(self, a1, a2):
        """
        """
        if len(a1) < len(a2):
            return self.longestCommonSubsequence(a2, a1)
        v1 = [[0 for v2 in range(len(a2) + 1)] for v2 in range(2)]
        for v3 in range(1, len(a1) + 1):
            for v4 in range(1, len(a2) + 1):
                v1[v3 % 2][v4] = v1[(v3 - 1) % 2][v4 - 1] + 1 if a1[v3 - 1] == a2[v4 - 1] else max(v1[(v3 - 1) % 2][v4], v1[v3 % 2][v4 - 1])
        return v1[len(a1) % 2][len(a2)]

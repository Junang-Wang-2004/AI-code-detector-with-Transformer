class C1(object):

    def longestSubsequence(self, a1):
        """
        """
        v1 = 2
        v2 = max(a1)
        v3 = [[0] * v2 for v4 in range(v2)]
        for v5 in a1:
            v5 -= 1
            for v6 in range(len(v3[v5])):
                v7 = abs(v6 - v5)
                v3[v5][v7] = max(v3[v5][v7], v3[v6][v7] + 1)
            for v7 in reversed(range(len(v3[v5]) - 1)):
                v3[v5][v7] = max(v3[v5][v7], v3[v5][v7 + 1])
            v1 = max(v1, v3[v5][0])
        return v1

class C1(object):

    def longestPalindromicSubsequence(self, a1, a2):
        """
        """
        v1 = [[[1 if i == j else 0 for v2 in range(a2 + 1)] for v3 in range(len(a1))] for v4 in range(len(a1))]
        for v4 in reversed(range(len(a1) - 1)):
            for v3 in range(v4 + 1, len(a1)):
                for v5 in range(a2 + 1):
                    if a1[v4] == a1[v3]:
                        v1[v4][v3][v5] = v1[v4 + 1][v3 - 1][v5] + 2
                    else:
                        v1[v4][v3][v5] = max(v1[v4 + 1][v3][v5], v1[v4][v3 - 1][v5])
                        v6 = abs(ord(a1[v4]) - ord(a1[v3]))
                        v7 = min(v6, 26 - v6)
                        if v5 >= v7:
                            v1[v4][v3][v5] = max(v1[v4][v3][v5], v1[v4 + 1][v3 - 1][v5 - v7] + 2)
        return v1[0][-1][a2]

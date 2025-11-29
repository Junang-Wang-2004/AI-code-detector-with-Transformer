class C1(object):

    def longestPalindromeSubseq(self, a1):
        """
        """
        v1 = [[[0] * 26 for v2 in range(len(a1))] for v2 in range(2)]
        for v3 in reversed(range(len(a1))):
            for v4 in range(v3 + 1, len(a1)):
                if v3 == v4 - 1:
                    if a1[v4] == a1[v3]:
                        v1[v3 % 2][v4][ord(a1[v3]) - ord('a')] = 2
                else:
                    for v5 in range(26):
                        if a1[v4] == a1[v3] and ord(a1[v4]) - ord('a') != v5:
                            v1[v3 % 2][v4][ord(a1[v4]) - ord('a')] = max(v1[v3 % 2][v4][ord(a1[v4]) - ord('a')], v1[(v3 + 1) % 2][v4 - 1][v5] + 2)
                        v1[v3 % 2][v4][v5] = max(v1[v3 % 2][v4][v5], v1[v3 % 2][v4 - 1][v5], v1[(v3 + 1) % 2][v4][v5], v1[(v3 + 1) % 2][v4 - 1][v5])
        return max(v1[0][-1])

class C1(object):

    def longestPalindrome(self, a1, a2):
        """
        """
        v1 = a1 + a2
        v2 = [[0] * len(v1) for v3 in range(len(v1))]
        v4 = 0
        for v5 in range(len(v1)):
            v2[v5][v5] = 1
            for v6 in reversed(range(v5)):
                if v1[v6] == v1[v5]:
                    v2[v6][v5] = 2 if v6 + 1 == v5 else v2[v6 + 1][v5 - 1] + 2
                    if v6 < len(a1) <= v5:
                        v4 = max(v4, v2[v6][v5])
                else:
                    v2[v6][v5] = max(v2[v6 + 1][v5], v2[v6][v5 - 1])
        return v4

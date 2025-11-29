class C1(object):

    def longestPalindrome(self, a1, a2):
        """
        """
        v1 = a1 + a2
        v2 = [[0] * len(v1) for v3 in range(len(v1))]
        for v4 in range(len(v1)):
            v2[v4][v4] = 1
            for v5 in reversed(range(v4)):
                if v1[v5] == v1[v4]:
                    v2[v5][v4] = 2 if v5 + 1 == v4 else v2[v5 + 1][v4 - 1] + 2
                else:
                    v2[v5][v4] = max(v2[v5 + 1][v4], v2[v5][v4 - 1])
        return max([v2[v5][v4] for v5 in range(len(a1)) for v4 in range(len(a1), len(v1)) if v1[v5] == v1[v4]] or [0])

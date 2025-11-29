class C1(object):

    def countPalindromicSubsequences(self, a1):
        """
        """

        def dp(a1, a2, a3, a4, a5):
            if a5[a1][a2] is not None:
                return a5[a1][a2]
            v1 = 1
            if a1 <= a2:
                for v2 in range(4):
                    v3 = a4[a1][v2]
                    v4 = a3[a2][v2]
                    if a1 <= v3 <= a2:
                        v1 = (v1 + 1) % P
                    if None < v3 < v4:
                        v1 = (v1 + dp(v3 + 1, v4 - 1, a3, a4, a5)) % P
            v1 %= P
            a5[a1][a2] = v1
            return v1
        v1 = [None] * len(a1)
        v2 = [None] * len(a1)
        v3 = [None] * 4
        for v4 in range(len(a1)):
            v3[ord(a1[v4]) - ord('a')] = v4
            v1[v4] = tuple(v3)
        v3 = [None] * 4
        for v4 in reversed(range(len(a1))):
            v3[ord(a1[v4]) - ord('a')] = v4
            v2[v4] = tuple(v3)
        v5 = 10 ** 9 + 7
        v6 = [[None] * len(a1) for v7 in range(len(a1))]
        return dp(0, len(a1) - 1, v1, v2, v6) - 1

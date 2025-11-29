class C1:

    def longestPalindromicSubsequence(self, a1, a2):
        v1 = len(a1)
        v2 = [[[0] * (a2 + 1) for v3 in range(v1)] for v3 in range(v1)]
        for v4 in range(v1):
            for v5 in range(a2 + 1):
                v2[v4][v4][v5] = 1
        for v6 in range(2, v1 + 1):
            for v7 in range(v1 - v6 + 1):
                v8 = v7 + v6 - 1
                for v5 in range(a2 + 1):
                    v9 = max(v2[v7 + 1][v8][v5], v2[v7][v8 - 1][v5])
                    v10 = abs(ord(a1[v7]) - ord(a1[v8]))
                    v11 = min(v10, 26 - v10)
                    if v5 >= v11:
                        v9 = max(v9, v2[v7 + 1][v8 - 1][v5 - v11] + 2)
                    v2[v7][v8][v5] = v9
        return v2[0][v1 - 1][a2]

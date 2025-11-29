class C1:

    def longestSubsequence(self, a1):
        v1 = max(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        v4 = 2
        for v5 in a1:
            v6 = v5 - 1
            v7 = 0
            for v8 in range(v1):
                v9 = 0
                if v6 - v8 >= 0:
                    v9 = max(v9, v2[v6 - v8][v8])
                if v6 + v8 < v1:
                    v9 = max(v9, v2[v6 + v8][v8])
                v2[v6][v8] = max(v2[v6][v8], v9 + 1)
                v7 = max(v7, v2[v6][v8])
            v4 = max(v4, v7)
        return v4

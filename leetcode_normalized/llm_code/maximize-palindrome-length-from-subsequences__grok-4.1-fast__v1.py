class C1:

    def longestPalindrome(self, a1, a2):
        v1 = a1 + a2
        v2 = len(v1)
        v3 = len(a1)
        v4 = [[0] * v2 for v5 in v2]
        v6 = 0
        for v7 in range(v2):
            v4[v7][v7] = 1
        for v8 in range(2, v2 + 1):
            for v9 in range(v2 - v8 + 1):
                v10 = v9 + v8 - 1
                if v1[v9] == v1[v10]:
                    v11 = 0 if v8 == 2 else v4[v9 + 1][v10 - 1]
                    v4[v9][v10] = 2 + v11
                    if v9 < v3 <= v10:
                        v6 = max(v6, v4[v9][v10])
                else:
                    v4[v9][v10] = max(v4[v9 + 1][v10], v4[v9][v10 - 1])
        return v6

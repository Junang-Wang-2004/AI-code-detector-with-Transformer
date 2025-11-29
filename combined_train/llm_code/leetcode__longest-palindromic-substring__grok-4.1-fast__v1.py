class C1:

    def longestPalindrome(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return ''
        v2 = [[False] * v1 for v3 in range(v1)]
        v4, v5 = (0, 1)
        for v6 in range(v1):
            v2[v6][v6] = True
        for v6 in range(v1 - 1):
            if a1[v6] == a1[v6 + 1]:
                v2[v6][v6 + 1] = True
                v4 = v6
                v5 = 2
        for v7 in range(3, v1 + 1):
            for v6 in range(v1 - v7 + 1):
                v8 = v6 + v7 - 1
                if a1[v6] == a1[v8] and v2[v6 + 1][v8 - 1]:
                    v2[v6][v8] = True
                    v4 = v6
                    v5 = v7
        return a1[v4:v4 + v5]

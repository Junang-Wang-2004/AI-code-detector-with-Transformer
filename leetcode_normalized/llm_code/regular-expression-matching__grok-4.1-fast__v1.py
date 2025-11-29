class C1:

    def isMatch(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = [[False] * (v2 + 1) for v4 in range(v1 + 1)]
        v3[0][0] = True
        for v5 in range(2, v2 + 1):
            if a2[v5 - 1] == '*':
                v3[0][v5] = v3[0][v5 - 2]
        for v6 in range(1, v1 + 1):
            for v5 in range(1, v2 + 1):
                if a2[v5 - 1] == '*':
                    v7 = v3[v6][v5 - 2]
                    v8 = (a1[v6 - 1] == a2[v5 - 2] or a2[v5 - 2] == '.') and v3[v6 - 1][v5]
                    v3[v6][v5] = v7 or v8
                else:
                    v9 = a1[v6 - 1] == a2[v5 - 1] or a2[v5 - 1] == '.'
                    v3[v6][v5] = v9 and v3[v6 - 1][v5 - 1]
        return v3[v1][v2]

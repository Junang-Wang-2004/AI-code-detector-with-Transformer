class C1(object):

    def lenOfVDiagonal(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4 = [[1] * v2 for v5 in range(v1)]
        v6 = [[1] * v2 for v5 in range(v1)]
        for v7 in range(v1):
            for v8 in range(v2):
                v9 = a1[v7][v8]
                if v9 == 1:
                    v3 = 1
                    continue
                if v7 - 1 >= 0 and v8 - 1 >= 0 and (a1[v7 - 1][v8 - 1] == 2 - v9):
                    v4[v7][v8] = v4[v7 - 1][v8 - 1] + 1
                if v7 - 1 >= 0 and v8 + 1 < v2 and (a1[v7 - 1][v8 + 1] == 2 - v9):
                    v6[v7][v8] = v6[v7 - 1][v8 + 1] + 1
        v10 = [[1] * v2 for v5 in range(v1)]
        v11 = [[1] * v2 for v5 in range(v1)]
        for v7 in reversed(range(v1)):
            for v8 in range(v2):
                v9 = a1[v7][v8]
                if v9 == 1:
                    continue
                if v7 + 1 < v1 and v8 - 1 >= 0 and (a1[v7 + 1][v8 - 1] == 2 - v9):
                    v10[v7][v8] = v10[v7 + 1][v8 - 1] + 1
                if v7 + 1 < v1 and v8 + 1 < v2 and (a1[v7 + 1][v8 + 1] == 2 - v9):
                    v11[v7][v8] = v11[v7 + 1][v8 + 1] + 1
        for v7 in range(v1):
            for v8 in range(v2):
                v9 = a1[v7][v8]
                if v9 == 1:
                    continue
                if v4[v7][v8] % 2 * 2 == 0 and v9 == 0 or (v4[v7][v8] % 2 == 1 and v9 == 2):
                    v12 = v7 - v4[v7][v8]
                    v13 = v8 - v4[v7][v8]
                    if 0 <= v12 < v1 and 0 <= v13 < v2 and (a1[v12][v13] == 1):
                        v3 = max(v3, v4[v7][v8] + v10[v7][v8])
                if v6[v7][v8] % 2 == 0 and v9 == 0 or (v6[v7][v8] % 2 == 1 and v9 == 2):
                    v12 = v7 - v6[v7][v8]
                    v13 = v8 + v6[v7][v8]
                    if 0 <= v12 < v1 and 0 <= v13 < v2 and (a1[v12][v13] == 1):
                        v3 = max(v3, v6[v7][v8] + v4[v7][v8])
                if v11[v7][v8] % 2 == 0 and v9 == 0 or (v11[v7][v8] % 2 == 1 and v9 == 2):
                    v12 = v7 + v11[v7][v8]
                    v13 = v8 + v11[v7][v8]
                    if 0 <= v12 < v1 and 0 <= v13 < v2 and (a1[v12][v13] == 1):
                        v3 = max(v3, v11[v7][v8] + v6[v7][v8])
                if v10[v7][v8] % 2 == 0 and v9 == 0 or (v10[v7][v8] % 2 == 1 and v9 == 2):
                    v12 = v7 + v10[v7][v8]
                    v13 = v8 - v10[v7][v8]
                    if 0 <= v12 < v1 and 0 <= v13 < v2 and (a1[v12][v13] == 1):
                        v3 = max(v3, v10[v7][v8] + v11[v7][v8])
        return v3

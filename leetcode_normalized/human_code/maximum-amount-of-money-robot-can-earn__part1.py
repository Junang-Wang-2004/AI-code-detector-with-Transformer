class C1(object):

    def maximumAmount(self, a1):
        """
        """
        v1 = 2
        v2 = min(len(a1), len(a1[0]))
        v3 = max(len(a1), len(a1[0]))
        v4 = (lambda i, j: a1[i][j]) if len(a1) == v3 else lambda i, j: a1[j][i]
        v5 = [[float('-inf')] * (v1 + 1) for v6 in range(v2)]
        for v7 in range(v3):
            v8 = [[float('-inf')] * (v1 + 1) for v6 in range(v2)]
            for v9 in range(v2):
                for v10 in range(v1 + 1):
                    if v7 == 0 and v9 == 0:
                        v8[v9][v10] = max(v4(v7, v9), 0) if v10 - 1 >= 0 else v4(v7, v9)
                        continue
                    if v7 - 1 >= 0:
                        v8[v9][v10] = max(v8[v9][v10], v5[v9][v10] + v4(v7, v9))
                        if v10 - 1 >= 0:
                            v8[v9][v10] = max(v8[v9][v10], v5[v9][v10 - 1])
                    if v9 - 1 >= 0:
                        v8[v9][v10] = max(v8[v9][v10], v8[v9 - 1][v10] + v4(v7, v9))
                        if v10 - 1 >= 0:
                            v8[v9][v10] = max(v8[v9][v10], v8[v9 - 1][v10 - 1])
            v5 = v8
        return v5[-1][-1]

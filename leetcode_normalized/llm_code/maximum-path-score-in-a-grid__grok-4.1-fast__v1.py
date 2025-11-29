class C1:

    def maxPathScore(self, a1, a2):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[[-1 for v4 in range(a2 + 1)] for v4 in range(v2)] for v4 in range(v1)]
        v3[0][0][0] = 0
        for v5 in range(v1):
            for v6 in range(v2):
                if v5 == 0 and v6 == 0:
                    continue
                v7 = 1 if a1[v5][v6] != 0 else 0
                if v6 > 0:
                    for v8 in range(v7, a2 + 1):
                        v9 = v8 - v7
                        v10 = v3[v5][v6 - 1][v9]
                        if v10 != -1:
                            v11 = v10 + a1[v5][v6]
                            if v3[v5][v6][v8] == -1 or v11 > v3[v5][v6][v8]:
                                v3[v5][v6][v8] = v11
                if v5 > 0:
                    for v8 in range(v7, a2 + 1):
                        v9 = v8 - v7
                        v10 = v3[v5 - 1][v6][v9]
                        if v10 != -1:
                            v11 = v10 + a1[v5][v6]
                            if v3[v5][v6][v8] == -1 or v11 > v3[v5][v6][v8]:
                                v3[v5][v6][v8] = v11
        return max(v3[-1][-1])

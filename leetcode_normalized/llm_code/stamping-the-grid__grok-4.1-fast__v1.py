class C1:

    def possibleToStamp(self, a1, a2, a3):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * (v2 + 1) for v4 in range(v1 + 1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v3[v5 + 1][v6 + 1] = v3[v5 + 1][v6] + v3[v5][v6 + 1] - v3[v5][v6] + (1 - a1[v5][v6])
        v7 = [[0] * v2 for v4 in range(v1)]
        for v5 in range(a2 - 1, v1):
            for v6 in range(a3 - 1, v2):
                v8 = v5 - a2 + 1
                v9 = v6 - a3 + 1
                v10 = v3[v5 + 1][v6 + 1] - v3[v8][v6 + 1] - v3[v5 + 1][v9] + v3[v8][v9]
                if v10 == a2 * a3:
                    v7[v5][v6] = 1
        v11 = [[0] * (v2 + 1) for v4 in range(v1 + 1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v11[v5 + 1][v6 + 1] = v11[v5 + 1][v6] + v11[v5][v6 + 1] - v11[v5][v6] + v7[v5][v6]
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] == 0:
                    v12 = min(v5 + a2, v1)
                    v13 = min(v6 + a3, v2)
                    v14 = v11[v12][v13] - v11[v5][v13] - v11[v12][v6] + v11[v5][v6]
                    if v14 == 0:
                        return False
        return True

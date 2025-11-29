class C1:

    def matrixBlockSum(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in a1:
            v5 = [0]
            for v6 in v4:
                v5.append(v5[-1] + v6)
            v3.append(v5)
        v7 = [[0] * (v2 + 1) for v8 in range(v1 + 1)]
        for v9 in range(v2 + 1):
            for v10 in range(v1):
                v7[v10 + 1][v9] = v7[v10][v9] + v3[v10][v9]
        v11 = [[0] * v2 for v8 in range(v1)]
        for v12 in range(v1):
            for v13 in range(v2):
                v14, v15 = (max(0, v12 - a2), max(0, v13 - a2))
                v16, v17 = (min(v1, v12 + a2 + 1), min(v2, v13 + a2 + 1))
                v11[v12][v13] = v7[v16][v17] - v7[v14][v17] - v7[v16][v15] + v7[v14][v15]
        return v11

class C1(object):

    def matrixBlockSum(self, a1, a2):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0 for v4 in range(v2 + 1)] for v4 in range(v1 + 1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v3[v5 + 1][v6 + 1] = v3[v5 + 1][v6] + v3[v5][v6 + 1] - v3[v5][v6] + a1[v5][v6]
        v7 = [[0 for v4 in range(v2)] for v4 in range(v1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v8, v9, v10, v11 = (max(v5 - a2, 0), max(v6 - a2, 0), min(v5 + a2 + 1, v1), min(v6 + a2 + 1, v2))
                v7[v5][v6] = v3[v10][v11] - v3[v8][v11] - v3[v10][v9] + v3[v8][v9]
        return v7

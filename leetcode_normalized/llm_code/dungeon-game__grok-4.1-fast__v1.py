class C1:

    def calculateMinimumHP(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]
        v3[v1 - 1][v2 - 1] = max(1, 1 - a1[v1 - 1][v2 - 1])
        for v5 in range(v2 - 2, -1, -1):
            v3[v1 - 1][v5] = max(1, v3[v1 - 1][v5 + 1] - a1[v1 - 1][v5])
        for v6 in range(v1 - 2, -1, -1):
            v3[v6][v2 - 1] = max(1, v3[v6 + 1][v2 - 1] - a1[v6][v2 - 1])
        for v6 in range(v1 - 2, -1, -1):
            for v5 in range(v2 - 2, -1, -1):
                v7 = min(v3[v6 + 1][v5], v3[v6][v5 + 1])
                v3[v6][v5] = max(1, v7 - a1[v6][v5])
        return v3[0][0]

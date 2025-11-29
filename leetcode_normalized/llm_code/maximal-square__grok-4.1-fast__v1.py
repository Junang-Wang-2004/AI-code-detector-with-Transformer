class C1:

    def maximalSquare(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]
        v5 = 0
        for v6 in range(v2):
            v3[0][v6] = 1 if a1[0][v6] == '1' else 0
            v5 = max(v5, v3[0][v6])
        for v7 in range(1, v1):
            v3[v7][0] = 1 if a1[v7][0] == '1' else 0
            v5 = max(v5, v3[v7][0])
        for v7 in range(1, v1):
            for v6 in range(1, v2):
                if a1[v7][v6] == '1':
                    v3[v7][v6] = min(v3[v7 - 1][v6], v3[v7][v6 - 1], v3[v7 - 1][v6 - 1]) + 1
                    v5 = max(v5, v3[v7][v6])
                else:
                    v3[v7][v6] = 0
        return v5 * v5

class C1:

    def mctFromLeafValues(self, a1):
        v1 = len(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            v2[v4][v4] = a1[v4]
        for v5 in range(2, v1 + 1):
            for v4 in range(v1 - v5 + 1):
                v6 = v4 + v5 - 1
                v2[v4][v6] = max(v2[v4][v6 - 1], a1[v6])
        v7 = [[0] * v1 for v3 in range(v1)]
        for v5 in range(2, v1 + 1):
            for v4 in range(v1 - v5 + 1):
                v6 = v4 + v5 - 1
                v8 = float('inf')
                for v9 in range(v4, v6):
                    v10 = v7[v4][v9] + v7[v9 + 1][v6] + v2[v4][v9] * v2[v9 + 1][v6]
                    if v10 < v8:
                        v8 = v10
                v7[v4][v6] = v8
        return v7[0][v1 - 1]

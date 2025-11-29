class C1:

    def minCost(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = max((max(row) for v4 in a1))
        v5 = [[float('inf')] * v2 for v6 in range(v1)]
        v5[0][0] = 0
        v7 = [float('inf')] * (v3 + 2)
        for v6 in range(a2 + 1):
            for v8 in range(v1):
                for v9 in range(v2):
                    v5[v8][v9] = min(v5[v8][v9], v7[a1[v8][v9]])
            for v8 in range(v1):
                for v9 in range(v2):
                    v10 = a1[v8][v9]
                    if v8 > 0:
                        v5[v8][v9] = min(v5[v8][v9], v5[v8 - 1][v9] + v10)
                    if v9 > 0:
                        v5[v8][v9] = min(v5[v8][v9], v5[v8][v9 - 1] + v10)
            v7 = [float('inf')] * (v3 + 2)
            for v8 in range(v1):
                for v9 in range(v2):
                    v7[a1[v8][v9]] = min(v7[a1[v8][v9]], v5[v8][v9])
            for v11 in range(v3, -1, -1):
                v7[v11] = min(v7[v11], v7[v11 + 1])
        return v5[v1 - 1][v2 - 1]

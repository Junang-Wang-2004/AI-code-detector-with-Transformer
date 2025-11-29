class C1:

    def stoneGameVII(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [[0] * v1 for v5 in range(v1)]
        for v6 in range(2, v1 + 1):
            for v7 in range(v1 - v6 + 1):
                v8 = v7 + v6 - 1
                v9 = v2[v8 + 1] - v2[v7 + 1]
                v10 = v2[v8] - v2[v7]
                v4[v7][v8] = max(v9 - v4[v7 + 1][v8], v10 - v4[v7][v8 - 1])
        return v4[0][v1 - 1]

class C1:

    def maximalNetworkRank(self, a1, a2):
        v1 = [0] * a1
        v2 = [[False] * a1 for v3 in range(a1)]
        for v4, v5 in a2:
            v1[v4] += 1
            v1[v5] += 1
            v2[v4][v5] = True
            v2[v5][v4] = True
        v6 = 0
        for v7 in range(a1):
            for v8 in range(v7 + 1, a1):
                v9 = 1 if v2[v7][v8] else 0
                v10 = v1[v7] + v1[v8] - v9
                v6 = max(v6, v10)
        return v6

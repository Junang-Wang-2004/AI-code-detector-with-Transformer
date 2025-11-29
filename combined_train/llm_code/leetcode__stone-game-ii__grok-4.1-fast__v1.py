class C1:

    def stoneGameII(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1 - 1, -1, -1):
            v2[v3] = a1[v3] + v2[v3 + 1]
        v4 = [[0] * (v1 + 1) for v5 in range(v1 + 1)]
        for v3 in range(v1 - 1, -1, -1):
            for v6 in range(1, v1 + 1):
                v7 = v1 - v3
                v8 = min(2 * v6, v7)
                if v8 >= v7:
                    v4[v3][v6] = v2[v3]
                    continue
                v9 = float('inf')
                for v10 in range(1, v8 + 1):
                    v11 = v3 + v10
                    v12 = max(v6, v10)
                    v9 = min(v9, v4[v11][v12])
                v4[v3][v6] = v2[v3] - v9
        return v4[0][1]

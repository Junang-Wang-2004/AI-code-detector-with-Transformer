class C1:

    def getMoneyAmount(self, a1):
        v1 = [[0] * (a1 + 2) for v2 in range(a1 + 2)]
        for v3 in range(2, a1 + 1):
            for v4 in range(1, a1 - v3 + 2):
                v5 = v4 + v3 - 1
                v6 = float('inf')
                for v7 in range(v4, v5 + 1):
                    v8 = v1[v4][v7 - 1]
                    v9 = v1[v7 + 1][v5]
                    v10 = v7 + max(v8, v9)
                    v6 = min(v6, v10)
                v1[v4][v5] = v6
        return v1[1][a1]

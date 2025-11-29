class C1:

    def minDistance(self, a1, a2):
        a1.sort()
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [[0] * v1 for v5 in range(v1)]
        for v6 in range(v1):
            for v7 in range(v6, v1):
                v8 = v7 - v6 + 1
                v9 = v6 + (v8 - 1) // 2
                v10 = v2[v9] - v2[v6]
                v11 = v9 - v6
                v12 = v2[v7 + 1] - v2[v9 + 1]
                v13 = v7 - v9
                v14 = a1[v9]
                v4[v6][v7] = v12 - v13 * v14 + v11 * v14 - v10
        v15 = 10 ** 18
        v16 = [[v15] * v1 for v5 in range(a2 + 1)]
        for v17 in range(v1):
            v16[1][v17] = v4[0][v17]
        for v18 in range(2, a2 + 1):
            for v17 in range(v18 - 1, v1):
                for v19 in range(v18 - 2, v17):
                    v16[v18][v17] = min(v16[v18][v17], v16[v18 - 1][v19] + v4[v19 + 1][v17])
        return v16[a2][v1 - 1]

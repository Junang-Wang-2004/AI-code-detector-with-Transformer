class C1:

    def largest1BorderedSquare(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [[0] * (v2 + 1) for v4 in range(v1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v3[v5][v6 + 1] = v3[v5][v6] + a1[v5][v6]
        v7 = [[0] * (v1 + 1) for v4 in range(v2)]
        for v6 in range(v2):
            for v5 in range(v1):
                v7[v6][v5 + 1] = v7[v6][v5] + a1[v5][v6]
        v8 = 0
        for v9 in range(v1):
            for v10 in range(v2):
                v11 = min(v1 - v9, v2 - v10)
                for v12 in range(1, v11 + 1):
                    v13 = v9
                    v14 = v9 + v12 - 1
                    v15 = v10
                    v16 = v10 + v12 - 1
                    v17 = v3[v13][v16 + 1] - v3[v13][v15] == v12
                    v18 = v3[v14][v16 + 1] - v3[v14][v15] == v12
                    v19 = v7[v15][v14 + 1] - v7[v15][v13] == v12
                    v20 = v7[v16][v14 + 1] - v7[v16][v13] == v12
                    if v17 and v18 and v19 and v20:
                        v8 = max(v8, v12)
        return v8 * v8

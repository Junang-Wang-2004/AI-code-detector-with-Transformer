class C1:

    def lenOfVDiagonal(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4 = [[1] * v2 for v5 in range(v1)]
        v6 = [[1] * v2 for v5 in range(v1)]
        for v7 in range(v1):
            for v8 in range(v2):
                v9 = a1[v7][v8]
                if v9 == 1:
                    v3 = max(v3, 1)
                    continue
                if v7 > 0 and v8 > 0 and (a1[v7 - 1][v8 - 1] == 2 - v9):
                    v4[v7][v8] = v4[v7 - 1][v8 - 1] + 1
                if v7 > 0 and v8 + 1 < v2 and (a1[v7 - 1][v8 + 1] == 2 - v9):
                    v6[v7][v8] = v6[v7 - 1][v8 + 1] + 1
        v10 = [[1] * v2 for v5 in range(v1)]
        v11 = [[1] * v2 for v5 in range(v1)]
        for v7 in range(v1 - 1, -1, -1):
            for v8 in range(v2):
                v9 = a1[v7][v8]
                if v9 == 1:
                    continue
                if v7 + 1 < v1 and v8 > 0 and (a1[v7 + 1][v8 - 1] == 2 - v9):
                    v10[v7][v8] = v10[v7 + 1][v8 - 1] + 1
                if v7 + 1 < v1 and v8 + 1 < v2 and (a1[v7 + 1][v8 + 1] == 2 - v9):
                    v11[v7][v8] = v11[v7 + 1][v8 + 1] + 1
        for v7 in range(v1):
            for v8 in range(v2):
                v9 = a1[v7][v8]
                if v9 == 1:
                    continue
                v12 = v4[v7][v8]
                if v12 % 2 == v9 // 2:
                    v13, v14 = (v7 - v12, v8 - v12)
                    if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == 1):
                        v3 = max(v3, v12 + v10[v7][v8])
                v15 = v6[v7][v8]
                if v15 % 2 == v9 // 2:
                    v13, v14 = (v7 - v15, v8 + v15)
                    if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == 1):
                        v3 = max(v3, v15 + v4[v7][v8])
                v16 = v11[v7][v8]
                if v16 % 2 == v9 // 2:
                    v13, v14 = (v7 + v16, v8 + v16)
                    if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == 1):
                        v3 = max(v3, v16 + v6[v7][v8])
                v17 = v10[v7][v8]
                if v17 % 2 == v9 // 2:
                    v13, v14 = (v7 + v17, v8 - v17)
                    if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == 1):
                        v3 = max(v3, v17 + v11[v7][v8])
        return v3

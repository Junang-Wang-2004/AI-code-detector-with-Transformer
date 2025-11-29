class C1:

    def stoneGameV(self, a1):
        v1 = len(a1)
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [[0] * v1 for v5 in range(v1)]
        v6 = [[0] * v1 for v5 in range(v1)]
        for v3 in range(v1):
            v6[v3][v3] = a1[v3]
        for v7 in range(2, v1 + 1):
            for v3 in range(v1 - v7 + 1):
                v8 = v3 + v7 - 1
                v9 = float('inf')
                v10 = 0
                for v11 in range(v3, v8):
                    v12 = v2[v11 + 1] - v2[v3]
                    v13 = v2[v8 + 1] - v2[v11 + 1]
                    if v12 < v13:
                        v14 = v4[v11 + 1][v8] + v6[v11 + 1][v8]
                        v15 = v6[v11 + 1][v8]
                    elif v13 < v12:
                        v14 = v4[v3][v11] + v6[v3][v11]
                        v15 = v6[v3][v11]
                    else:
                        v16 = v4[v3][v11] + v6[v3][v11]
                        v17 = v4[v11 + 1][v8] + v6[v11 + 1][v8]
                        v14 = min(v16, v17)
                        if v16 <= v17:
                            v15 = v6[v3][v11]
                        else:
                            v15 = v6[v11 + 1][v8]
                    if v14 < v9:
                        v9 = v14
                        v10 = v15
                v18 = v2[v8 + 1] - v2[v3]
                v4[v3][v8] = v18 - v9
                v6[v3][v8] = v10
        return v4[0][v1 - 1]

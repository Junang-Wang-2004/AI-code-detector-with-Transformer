class C1:

    def removeBoxes(self, a1):
        v1 = len(a1)
        v2 = [[[0] * (v1 + 1) for v3 in range(v1)] for v3 in range(v1)]
        for v4 in range(1, v1 + 1):
            for v5 in range(v1 - v4 + 1):
                v6 = v5 + v4 - 1
                for v7 in range(v1 - v4 + 1):
                    v8 = a1[v5]
                    v9 = 1
                    while v5 + v9 <= v6 and a1[v5 + v9] == v8:
                        v9 += 1
                    v10 = v5 + v9 - 1
                    v11 = (v7 + v9) ** 2
                    if v10 + 1 <= v6:
                        v11 += v2[v10 + 1][v6][0]
                    for v12 in range(v10 + 1, v6 + 1):
                        if a1[v12] == v8:
                            v13 = v10 + 1
                            v14 = v12 - 1
                            v15 = 0 if v13 > v14 else v2[v13][v14][0]
                            v16 = v7 + v9
                            v17 = v2[v12][v6][v16]
                            v11 = max(v11, v15 + v17)
                    v2[v5][v6][v7] = v11
        return v2[0][v1 - 1][0]

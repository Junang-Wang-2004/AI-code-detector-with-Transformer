class C1:

    def cherryPickup(self, a1):
        v1 = len(a1)
        v2 = [[-1] * v1 for v3 in range(v1)]
        v2[0][0] = a1[0][0]
        v4 = 2 * (v1 - 1)
        for v5 in range(1, v4 + 1):
            v6 = [[-1] * v1 for v3 in range(v1)]
            v7 = max(0, v5 - v1 + 1)
            v8 = min(v5, v1 - 1)
            for v9 in range(v7, v8 + 1):
                v10 = v5 - v9
                if a1[v9][v10] == -1:
                    continue
                for v11 in range(v7, v8 + 1):
                    v12 = v5 - v11
                    if a1[v11][v12] == -1:
                        continue
                    v13 = a1[v9][v10]
                    if v9 != v11:
                        v13 += a1[v11][v12]
                    v14 = -1
                    for v15 in (0, -1):
                        for v16 in (0, -1):
                            v17 = v9 + v15
                            v18 = v11 + v16
                            if v17 >= 0 and v18 >= 0 and (v2[v17][v18] != -1):
                                v14 = max(v14, v2[v17][v18] + v13)
                    v6[v9][v11] = v14
            v2 = v6
        return max(v2[v1 - 1][v1 - 1], 0)

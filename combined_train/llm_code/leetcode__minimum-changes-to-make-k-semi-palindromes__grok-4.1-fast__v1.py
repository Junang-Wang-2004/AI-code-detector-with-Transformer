class C1:

    def minimumChanges(self, a1: str, a2: int) -> int:
        v1 = len(a1)
        v2 = v1 + 1
        v3 = [[] for v4 in range(v1 + 1)]
        for v5 in range(1, v1 + 1):
            v6 = v5
            while v6 <= v1:
                v3[v6].append(v5)
                v6 += v5
        v7 = [[v2] * v1 for v4 in range(v1)]
        for v8 in range(1, v1 + 1):
            for v9 in range(v1 - v8 + 1):
                v10 = v9 + v8 - 1
                for v11 in v3[v8]:
                    if v11 == v8:
                        continue
                    v12 = v8 // v11
                    v13 = 0
                    for v14 in range(v12 // 2):
                        v15 = v9 + v14 * v11
                        v16 = v9 + (v12 - 1 - v14) * v11
                        for v17 in range(v11):
                            if a1[v15 + v17] != a1[v16 + v17]:
                                v13 += 1
                    v7[v9][v10] = min(v7[v9][v10], v13)
        v18 = [[v2] * (a2 + 1) for v4 in range(v1 + 1)]
        v18[0][0] = 0
        for v19 in range(1, a2 + 1):
            for v20 in range(1, v1 + 1):
                for v21 in range(v20):
                    v22 = v7[v21][v20 - 1]
                    if v22 < v2 and v18[v21][v19 - 1] < v2:
                        v18[v20][v19] = min(v18[v20][v19], v18[v21][v19 - 1] + v22)
        v23 = v18[v1][a2]
        return v23 if v23 < v2 else v1

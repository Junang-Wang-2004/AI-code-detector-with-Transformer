class C1:

    def resultGrid(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]
        v5 = [[0] * v2 for v4 in range(v1)]
        for v6 in range(1, v1 - 1):
            for v7 in range(1, v2 - 1):
                v8 = True
                for v9 in range(3):
                    for v10 in range(2):
                        v11, v12 = (v6 - 1 + v10, v6 - 1 + v10 + 1)
                        if abs(a1[v11][v7 - 1 + v9] - a1[v12][v7 - 1 + v9]) > a2:
                            v8 = False
                            break
                    if not v8:
                        break
                if not v8:
                    continue
                for v10 in range(3):
                    for v9 in range(2):
                        v13, v14 = (v7 - 1 + v9, v7 - 1 + v9 + 1)
                        if abs(a1[v6 - 1 + v10][v13] - a1[v6 - 1 + v10][v14]) > a2:
                            v8 = False
                            break
                    if not v8:
                        break
                if not v8:
                    continue
                v15 = sum((a1[v6 - 1 + dy][v7 - 1 + dx] for v16 in range(3) for v17 in range(3)))
                v18 = v15 // 9
                for v16 in range(3):
                    for v17 in range(3):
                        v19, v20 = (v6 - 1 + v16, v7 - 1 + v17)
                        v3[v19][v20] += v18
                        v5[v19][v20] += 1
        for v21 in range(v1):
            for v22 in range(v2):
                if v5[v21][v22] > 0:
                    v3[v21][v22] //= v5[v21][v22]
                else:
                    v3[v21][v22] = a1[v21][v22]
        return v3

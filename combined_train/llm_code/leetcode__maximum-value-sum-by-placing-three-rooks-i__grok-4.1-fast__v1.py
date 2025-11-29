class C1:

    def maximumValueSum(self, a1):
        v1 = 3
        v2 = len(a1)
        v3 = len(a1[0])
        v4 = []
        for v5 in range(v2):
            v6 = [(a1[v5][col_idx], v5, col_idx) for v7 in range(v3)]
            v6.sort(key=lambda x: x[0], reverse=True)
            v4.append(v6[:v1])
        v8 = [[] for v9 in range(v3)]
        for v10 in v4:
            for v11 in v10:
                v7 = v11[2]
                v8[v7].append(v11)
        for v7 in range(v3):
            v8[v7].sort(key=lambda x: x[0], reverse=True)
            v8[v7] = v8[v7][:v1]
        v12 = []
        for v13 in v8:
            v12.extend(v13)
        v12.sort(key=lambda x: x[0], reverse=True)
        v14 = (v1 - 1) * (2 * v1 - 1) + 1
        v15 = v12[:v14]
        v16 = 0
        v17 = len(v15)
        for v18 in range(v17):
            v19, v20, v21 = v15[v18]
            for v22 in range(v18 + 1, v17):
                v23, v24, v25 = v15[v22]
                if v20 == v24 or v21 == v25:
                    continue
                for v26 in range(v22 + 1, v17):
                    v27, v28, v29 = v15[v26]
                    if v28 == v20 or v28 == v24 or v29 == v21 or (v29 == v25):
                        continue
                    v16 = max(v16, v19 + v23 + v27)
        return v16

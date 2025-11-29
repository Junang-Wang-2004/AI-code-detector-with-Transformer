class C1:

    def countPairs(self, a1, a2, a3):
        v1 = [0] * (a1 + 1)
        v2 = {}
        for v3, v4 in a2:
            v1[v3] += 1
            v1[v4] += 1
            v5, v6 = (min(v3, v4), max(v3, v4))
            v7 = (v5, v6)
            v2[v7] = v2.get(v7, 0) + 1
        v8 = [v1[i] for v9 in range(1, a1 + 1)]
        if not v8:
            return [0] * len(a3)
        v10 = max(v8)
        v11 = [0] * (2 * (v10 + 2))
        v12 = {}
        for v13 in v8:
            v12[v13] = v12.get(v13, 0) + 1
        v14 = sorted(v12)
        for v9 in range(len(v14)):
            v15 = v14[v9]
            v16 = v12[v15]
            for v17 in range(v9, len(v14)):
                v18 = v14[v17]
                v19 = v12[v18]
                v20 = v15 + v18
                if v9 == v17:
                    v11[v20] += v16 * (v16 - 1) // 2
                else:
                    v11[v20] += v16 * v19
        for (v21, v22), v23 in v2.items():
            v24 = v1[v21] + v1[v22]
            v25 = v24 - v23
            v11[v24] -= 1
            if v25 >= 0:
                v11[v25] += 1
        for v26 in range(len(v11) - 2, -1, -1):
            v11[v26] += v11[v26 + 1]
        v27 = []
        for v28 in a3:
            v29 = v28 + 1
            v27.append(v11[v29] if v29 < len(v11) else 0)
        return v27

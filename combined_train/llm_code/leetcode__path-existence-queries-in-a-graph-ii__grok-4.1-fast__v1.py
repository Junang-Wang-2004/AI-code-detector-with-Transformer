class C1:

    def pathExistenceQueries(self, a1, a2, a3, a4):
        v1 = sorted(range(a1), key=lambda x: a2[x])
        v2 = [0] * a1
        for v3, v4 in enumerate(v1):
            v2[v4] = v3
        v5 = [0] * a1
        for v6 in range(1, a1):
            if a2[v1[v6]] - a2[v1[v6 - 1]] > a3:
                v5[v6] = v5[v6 - 1] + 1
            else:
                v5[v6] = v5[v6 - 1]
        v7 = [0] * a1
        v3 = 0
        for v8 in range(a1):
            while v3 < a1 and a2[v1[v3]] - a2[v1[v8]] <= a3:
                v3 += 1
            v7[v8] = v3 - 1
        v9 = 0
        while 1 << v9 <= a1:
            v9 += 1
        v10 = [[0] * a1 for v11 in range(v9)]
        for v6 in range(a1):
            v10[0][v6] = v7[v6]
        for v12 in range(1, v9):
            for v6 in range(a1):
                v10[v12][v6] = v10[v12 - 1][v10[v12 - 1][v6]]
        v13 = [-1] * len(a4)
        for v14, (v15, v16) in enumerate(a4):
            if v15 == v16:
                v13[v14] = 0
                continue
            v17 = v2[v15]
            v18 = v2[v16]
            if v17 > v18:
                v17, v18 = (v18, v17)
            if v5[v17] != v5[v18]:
                continue
            v19 = 0
            v20 = v17
            for v12 in range(v9 - 1, -1, -1):
                if v10[v12][v20] < v18:
                    v20 = v10[v12][v20]
                    v19 += 1 << v12
            v13[v14] = v19 + 1
        return v13

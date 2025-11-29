class C1(object):

    def maxActiveSectionsAfterTrade(self, a1, a2):
        v1 = len(a1)
        v2 = []
        v3 = 0
        v4 = 0
        while v3 < v1:
            if a1[v3] == '1':
                v4 += 1
                v3 += 1
                continue
            v5 = v3
            while v3 < v1 and a1[v3] == '0':
                v3 += 1
            v2.append((v5, v3 - v5))
        v6 = len(v2)
        v7 = [-1] * v1
        v8 = 0
        for v3 in range(v1):
            while v8 < v6 and v2[v8][0] <= v3:
                v8 += 1
            v7[v3] = v8 - 1
        if v6 < 2:
            return [v4] * len(a2)
        v9 = [v2[j][1] + v2[j + 1][1] for v10 in range(v6 - 1)]
        v11 = len(v9)
        v12 = 0
        while 1 << v12 <= v11:
            v12 += 1
        v13 = [[0] * v11 for v14 in range(v12)]
        v13[0] = v9[:]
        for v15 in range(1, v12):
            for v16 in range(v11 - (1 << v15) + 1):
                v13[v15][v16] = max(v13[v15 - 1][v16], v13[v15 - 1][v16 + (1 << v15 - 1)])

        def range_max(a1, a2):
            if a1 > a2:
                return 0
            v1 = a2 - a1 + 1
            v2 = 0
            while 1 << v2 + 1 <= v1:
                v2 += 1
            return max(v13[v2][a1], v13[v2][a2 - (1 << v2) + 1])
        v17 = len(a2)
        v18 = [v4] * v17
        for v19 in range(v17):
            v20, v21 = a2[v19]
            v22 = v7[v20]
            v23 = v7[v21]
            v24 = v22 + 1
            v25 = v23 - (1 if a1[v21] == '0' else 0)
            v26 = range_max(v24, v25 - 1)
            if a1[v20] == '0' and v22 >= 0:
                v27, v28 = v2[v22]
                v29 = v28 - (v20 - v27)
                v30 = v22 + 1
                if v30 < v6 and v30 <= v25:
                    v26 = max(v26, v29 + v2[v30][1])
            if a1[v21] == '0' and v23 >= 0:
                v31, v32 = v2[v23]
                v33 = v21 - v31 + 1
                v34 = v23 - 1
                if v34 >= 0 and v24 <= v34:
                    v26 = max(v26, v33 + v2[v34][1])
            if a1[v20] == '0' and a1[v21] == '0' and (v22 + 1 == v23) and (v22 >= 0):
                v27, v28 = v2[v22]
                v29 = v28 - (v20 - v27)
                v31, v32 = v2[v23]
                v33 = v21 - v31 + 1
                v26 = max(v26, v29 + v33)
            v18[v19] = v4 + v26
        return v18

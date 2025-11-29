import bisect

class C1:

    def maximumWeight(self, a1):
        v1 = 4
        v2 = {}
        v3 = []
        for v4, (v5, v6, v7) in enumerate(a1):
            v8 = (v5, v6, v7)
            if v8 not in v2:
                v2[v8] = v4
                v3.append((v6, v5, v7, v4))
        v3.sort(key=lambda x: x[0])
        v9 = len(v3)
        v10 = 2 * 10 ** 9 + 7
        v11 = [[(0, []) for v12 in range(v1 + 1)] for v12 in range(v9 + 1)]
        for v13 in range(v9):
            v12, v14, v15, v16 = v3[v13]
            v17 = bisect.bisect_right(v3, (v14, v10, v10, v10)) - 1
            for v18 in range(1, v1 + 1):
                v19, v20 = v11[v17 + 1][v18 - 1]
                v21 = v19 - v15
                v22 = v20[:]
                bisect.insort(v22, v16)
                v23, v24 = v11[v13][v18]
                v11[v13 + 1][v18] = (v21, v22) if v21 < v23 else (v23, v24)
        return v11[v9][v1][1]

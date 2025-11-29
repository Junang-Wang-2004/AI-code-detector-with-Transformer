class C1:

    def minCost(self, a1, a2):
        v1 = len(a2[0])
        v2 = [[0] * v1 for v3 in range(v1)]
        v4 = a1 // 2
        for v5 in range(v4):
            v6 = [[float('inf')] * v1 for v3 in range(v1)]
            v7 = a2[v5]
            v8 = a2[a1 - 1 - v5]
            for v9 in range(v1):
                for v10 in range(v1):
                    if v9 == v10:
                        continue
                    v11 = float('inf')
                    for v12 in range(v1):
                        if v12 == v9:
                            continue
                        for v13 in range(v1):
                            if v13 == v10 or v12 == v13:
                                continue
                            v11 = min(v11, v2[v12][v13])
                    v6[v9][v10] = v11 + v7[v9] + v8[v10]
            v2 = v6
        v14 = float('inf')
        for v15 in range(v1):
            for v16 in range(v1):
                if v15 != v16:
                    v14 = min(v14, v2[v15][v16])
        return v14

class C1(object):

    def minCost(self, a1, a2, a3, a4, a5):
        v1 = float('inf')
        v2 = [[v1] * a4 for v3 in range(a5)]
        v4 = range(a4) if a1[0] == 0 else [a1[0] - 1]
        for v5 in v4:
            v2[0][v5] = a2[0][v5] if a1[0] == 0 else 0
        for v6 in range(1, a3):
            v7 = [[v1] * a4 for v3 in range(a5)]
            for v8 in range(a5):
                for v9 in range(a4):
                    if v2[v8][v9] == v1:
                        continue
                    v10 = range(a4) if a1[v6] == 0 else [a1[v6] - 1]
                    for v11 in v10:
                        v12 = v8 + (v9 != v11)
                        if v12 >= a5:
                            continue
                        v13 = a2[v6][v11] if a1[v6] == 0 else 0
                        v7[v12][v11] = min(v7[v12][v11], v2[v8][v9] + v13)
            v2 = v7
        v14 = min(v2[a5 - 1])
        return v14 if v14 < v1 else -1

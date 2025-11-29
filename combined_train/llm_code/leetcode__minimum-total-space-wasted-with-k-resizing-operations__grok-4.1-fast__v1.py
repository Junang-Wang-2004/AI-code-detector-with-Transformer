class C1(object):

    def minSpaceWastedKResizing(self, a1, a2):
        v1 = len(a1)
        v2 = float('inf')
        v3 = [[0] * (v1 + 1) for v4 in range(v1)]
        for v5 in range(v1):
            v6 = 0
            v7 = 0
            for v8 in range(v5 + 1, v1 + 1):
                v7 += a1[v8 - 1]
                v6 = max(v6, a1[v8 - 1])
                v3[v5][v8] = v6 * (v8 - v5) - v7
        v9 = a2 + 1
        v10 = [[v2] * (v9 + 1) for v4 in range(v1 + 1)]
        v10[0][0] = 0
        for v11 in range(1, v9 + 1):
            for v12 in range(1, v1 + 1):
                for v13 in range(v12 + 1):
                    if v10[v13][v11 - 1] < v2:
                        v10[v12][v11] = min(v10[v12][v11], v10[v13][v11 - 1] + v3[v13][v12])
        return v10[v1][v9]

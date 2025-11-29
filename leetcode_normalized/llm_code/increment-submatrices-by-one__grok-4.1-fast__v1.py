class C1:

    def rangeAddQueries(self, a1, a2):
        v1 = [[0] * a1 for v2 in range(a1)]
        for v3, v4, v5, v6 in a2:
            v1[v3][v4] += 1
            if v6 + 1 < a1:
                v1[v3][v6 + 1] -= 1
            if v5 + 1 < a1:
                v1[v5 + 1][v4] -= 1
            if v5 + 1 < a1 and v6 + 1 < a1:
                v1[v5 + 1][v6 + 1] += 1
        for v7 in range(a1):
            v8 = 0
            for v9 in range(a1):
                v8 += v1[v7][v9]
                v1[v7][v9] = v8
        for v9 in range(a1):
            v8 = 0
            for v7 in range(a1):
                v8 += v1[v7][v9]
                v1[v7][v9] = v8
        return v1

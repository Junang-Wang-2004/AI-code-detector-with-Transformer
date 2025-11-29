class C1:

    def beautifulSplits(self, a1):
        v1 = len(a1)
        if v1 < 3:
            return 0
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(1, v1):
            for v5 in range(v1 - v4 - 1, -1, -1):
                v6 = v5 + v4
                if a1[v5] == a1[v6]:
                    v7 = v2[v5 + 1][v6 + 1] if v6 + 1 < v1 else 0
                    v2[v5][v6] = 1 + v7
        v8 = 0
        for v9 in range(1, v1 - 1):
            for v10 in range(v9 + 1, v1):
                v11 = v9
                v12 = v10 - v9
                v13 = v2[0][v9] >= v11 and v12 >= v11
                v14 = v2[v9][v10] >= v12
                if v13 or v14:
                    v8 += 1
        return v8

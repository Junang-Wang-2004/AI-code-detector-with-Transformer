class C1:

    def minFlips(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4, v5 = (v1 // 2, v2 // 2)
        for v6 in range(v4):
            for v7 in range(v5):
                v8 = a1[v6][v7]
                v9 = a1[v6][v2 - 1 - v7]
                v10 = a1[v1 - 1 - v6][v7]
                v11 = a1[v1 - 1 - v6][v2 - 1 - v7]
                v12 = v8 + v9 + v10 + v11
                v3 += min(v12, 4 - v12)
        v13 = 0
        v14 = 0
        if v1 % 2 == 1:
            v15 = v4
            for v7 in range(v5):
                v16 = a1[v15][v7]
                v17 = a1[v15][v2 - 1 - v7]
                v13 += v16 ^ v17
                v14 += v16 + v17
        if v2 % 2 == 1:
            v18 = v5
            for v6 in range(v4):
                v16 = a1[v6][v18]
                v17 = a1[v1 - 1 - v6][v18]
                v13 += v16 ^ v17
                v14 += v16 + v17
        if v1 % 2 == 1 and v2 % 2 == 1:
            v3 += a1[v4][v5]
        if v13 == 0:
            v3 += -v14 % 4
        v3 += v13
        return v3

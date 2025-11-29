class C1:

    def getMaxFunctionValue(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = a2 + 1
        while v3 > 0:
            v2 += 1
            v3 >>= 1
        v4 = [[0] * v1 for v5 in range(v2)]
        v6 = [[0] * v1 for v5 in range(v2)]
        for v7 in range(v1):
            v4[0][v7] = a1[v7]
            v6[0][v7] = v7
        for v8 in range(1, v2):
            for v7 in range(v1):
                v9 = v4[v8 - 1][v7]
                v4[v8][v7] = v4[v8 - 1][v9]
                v6[v8][v7] = v6[v8 - 1][v7] + v6[v8 - 1][v9]
        v10 = 0
        for v11 in range(v1):
            v12 = 0
            v13 = v11
            v14 = a2 + 1
            v8 = 0
            while v14 > 0 and v8 < v2:
                if v14 & 1:
                    v12 += v6[v8][v13]
                    v13 = v4[v8][v13]
                v14 >>= 1
                v8 += 1
            if v12 > v10:
                v10 = v12
        return v10

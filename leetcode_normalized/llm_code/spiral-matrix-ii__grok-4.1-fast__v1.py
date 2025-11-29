class C1:

    def generateMatrix(self, a1):
        v1 = [[0] * a1 for v2 in range(a1)]
        v3, v4 = (0, 0)
        v5 = [0, 1, 0, -1]
        v6 = [1, 0, -1, 0]
        v7 = 0
        for v8 in range(1, a1 * a1 + 1):
            v1[v3][v4] = v8
            v9 = v3 + v5[v7]
            v10 = v4 + v6[v7]
            if not (0 <= v9 < a1 and 0 <= v10 < a1 and (v1[v9][v10] == 0)):
                v7 = (v7 + 1) % 4
                v9 = v3 + v5[v7]
                v10 = v4 + v6[v7]
            v3, v4 = (v9, v10)
        return v1

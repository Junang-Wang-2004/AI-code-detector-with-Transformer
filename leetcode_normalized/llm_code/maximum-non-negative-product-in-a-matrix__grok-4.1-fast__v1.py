class C1:

    def maxProductPath(self, a1):
        v1 = 10 ** 9 + 7
        if not a1 or not a1[0]:
            return 0
        v2, v3 = (len(a1), len(a1[0]))
        v4 = [[0] * v3 for v5 in range(v2)]
        v6 = [[0] * v3 for v5 in range(v2)]
        v4[0][0] = v6[0][0] = a1[0][0]
        for v7 in range(1, v3):
            v8 = a1[0][v7]
            v9 = v4[0][v7 - 1] * v8
            v10 = v6[0][v7 - 1] * v8
            v4[0][v7] = max(v9, v10)
            v6[0][v7] = min(v9, v10)
        for v11 in range(1, v2):
            v8 = a1[v11][0]
            v9 = v4[v11 - 1][0] * v8
            v10 = v6[v11 - 1][0] * v8
            v4[v11][0] = max(v9, v10)
            v6[v11][0] = min(v9, v10)
        for v11 in range(1, v2):
            for v7 in range(1, v3):
                v8 = a1[v11][v7]
                v12 = v4[v11 - 1][v7] * v8
                v13 = v6[v11 - 1][v7] * v8
                v14 = v4[v11][v7 - 1] * v8
                v15 = v6[v11][v7 - 1] * v8
                v16 = [v12, v13, v14, v15]
                v4[v11][v7] = max(v16)
                v6[v11][v7] = min(v16)
        v17 = v4[v2 - 1][v3 - 1]
        return v17 % v1 if v17 >= 0 else -1

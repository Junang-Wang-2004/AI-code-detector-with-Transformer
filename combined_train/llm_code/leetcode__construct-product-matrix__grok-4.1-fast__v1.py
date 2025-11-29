class C1:

    def constructProductMatrix(self, a1):
        v1 = 12345
        v2 = len(a1)
        v3 = len(a1[0])
        v4 = [1] * v2
        for v5 in range(v2):
            for v6 in range(v3):
                v4[v5] = v4[v5] * a1[v5][v6] % v1
        v7 = [1] * (v2 + 1)
        for v5 in range(v2):
            v7[v5 + 1] = v7[v5] * v4[v5] % v1
        v8 = [1] * (v2 + 1)
        v8[v2] = 1
        for v5 in range(v2 - 1, -1, -1):
            v8[v5] = v8[v5 + 1] * v4[v5] % v1
        for v5 in range(v2):
            v9 = v7[v5] * v8[v5 + 1] % v1
            v10 = [1] * (v3 + 1)
            for v6 in range(v3):
                v10[v6 + 1] = v10[v6] * a1[v5][v6] % v1
            v11 = [1] * (v3 + 1)
            v11[v3] = 1
            for v6 in range(v3 - 1, -1, -1):
                v11[v6] = v11[v6 + 1] * a1[v5][v6] % v1
            for v6 in range(v3):
                a1[v5][v6] = v9 * v10[v6] * v11[v6 + 1] % v1
        return a1

class C1:

    def minimizeConcatenatedLength(self, a1):
        v1 = sum((len(w) for v2 in a1))
        v3 = len(a1)
        if v3 == 0:
            return 0
        v4 = [[float('-inf')] * 26 for v5 in range(2)]
        v6 = ord('a')
        v7, v8 = (ord(a1[0][0]) - v6, ord(a1[0][-1]) - v6)
        v4[0][v8] = v4[1][v7] = 0
        for v9 in range(1, v3):
            v10 = [[float('-inf')] * 26 for v5 in range(2)]
            v11, v12 = (ord(a1[v9 - 1][0]) - v6, ord(a1[v9 - 1][-1]) - v6)
            v13, v14 = (ord(a1[v9][0]) - v6, ord(a1[v9][-1]) - v6)
            for v15 in range(2):
                for v16 in range(26):
                    if v4[v15][v16] == float('-inf'):
                        continue
                    v17 = v16 if v15 else v11
                    v18 = v16 if v15 == 0 else v12
                    v10[1][v17] = max(v10[1][v17], v4[v15][v16] + (1 if v18 == v13 else 0))
                    v10[0][v18] = max(v10[0][v18], v4[v15][v16] + (1 if v14 == v17 else 0))
            v4 = v10
        return v1 - max((max(r) for v19 in v4))

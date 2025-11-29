class C1:

    def differByOne(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 131
        v3 = len(a1)
        if v3 < 2:
            return False
        v4 = len(a1[0])
        v5 = [1] * (v4 + 1)
        for v6 in range(1, v4 + 1):
            v5[v6] = v5[v6 - 1] * v2 % v1
        v7 = []
        for v8 in a1:
            v9 = [0] * (v4 + 1)
            for v10 in range(v4):
                v9[v10 + 1] = (v9[v10] * v2 + (ord(v8[v10]) - ord('a'))) % v1
            v7.append(v9)
        for v11 in range(v4):
            v12 = {}
            for v13 in range(v3):
                v14 = v7[v13][v11]
                v15 = v4 - v11 - 1
                v16 = v7[v13][v11 + 1] * v5[v15] % v1
                v17 = (v7[v13][v4] - v16 + v1) % v1
                v18 = (v14 * v5[v15] % v1 + v17) % v1
                if v18 in v12:
                    for v19 in v12[v18]:
                        v20 = a1[v19][:v11] + a1[v19][v11 + 1:]
                        v21 = a1[v13][:v11] + a1[v13][v11 + 1:]
                        if v20 == v21:
                            return True
                v12.setdefault(v18, []).append(v13)
        return False

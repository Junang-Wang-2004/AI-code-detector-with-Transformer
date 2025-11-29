class C1:

    def rotateGrid(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        for v3 in range(v1 // 2):
            v4 = v3
            v5 = v1 - v3 - 1
            v6 = v3
            v7 = v2 - v3 - 1
            v8 = 2 * (v5 - v4 + (v7 - v6))
            v9 = a2 % v8
            if v9 == 0:
                continue
            v10 = []
            for v11 in range(v4, v5):
                v10.append(a1[v11][v6])
            for v12 in range(v6, v7):
                v10.append(a1[v5][v12])
            for v11 in range(v5, v4, -1):
                v10.append(a1[v11][v7])
            for v12 in range(v7, v6, -1):
                v10.append(a1[v4][v12])
            v10 = v10[-v9:] + v10[:-v9]
            v13 = 0
            for v11 in range(v4, v5):
                a1[v11][v6] = v10[v13]
                v13 += 1
            for v12 in range(v6, v7):
                a1[v5][v12] = v10[v13]
                v13 += 1
            for v11 in range(v5, v4, -1):
                a1[v11][v7] = v10[v13]
                v13 += 1
            for v12 in range(v7, v6, -1):
                a1[v4][v12] = v10[v13]
                v13 += 1
        return a1

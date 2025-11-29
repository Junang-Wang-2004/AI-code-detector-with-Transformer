class C1(object):

    def mostSimilar(self, a1, a2, a3, a4):
        v1 = len(a4)
        v2 = v1 + 1
        v3 = [[] for v4 in range(a1)]
        for v5, v6 in a2:
            v3[v5].append(v6)
            v3[v6].append(v5)
        v7 = [[v2] * a1 for v4 in range(v1)]
        v8 = [[-1] * a1 for v4 in range(v1)]
        for v9 in range(a1):
            v7[0][v9] = 0 if a3[v9] == a4[0] else 1
        for v10 in range(1, v1):
            for v9 in range(a1):
                v11 = 0 if a3[v9] == a4[v10] else 1
                v12 = v2
                v13 = -1
                for v14 in v3[v9]:
                    if v7[v10 - 1][v14] < v12:
                        v12 = v7[v10 - 1][v14]
                        v13 = v14
                if v13 != -1:
                    v7[v10][v9] = v11 + v12
                    v8[v10][v9] = v13
        v15 = v2
        v16 = -1
        for v9 in range(a1):
            if v7[v1 - 1][v9] < v15:
                v15 = v7[v1 - 1][v9]
                v16 = v9
        v17 = []
        v18 = v16
        for v10 in range(v1 - 1, -1, -1):
            v17.append(v18)
            if v10 > 0:
                v18 = v8[v10][v18]
        v17.reverse()
        return v17

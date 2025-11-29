class C1:

    def pathsWithMaxScore(self, a1):
        v1 = 10 ** 9 + 7
        v2, v3 = (len(a1), len(a1[0]))
        v4 = [[[0, 0] for v5 in range(v3)] for v5 in range(v2)]
        if a1[0][0] not in 'XS':
            v6 = 0 if a1[0][0] == 'E' else int(a1[0][0])
            v4[0][0] = [v6, 1]
        for v7 in range(v2):
            for v8 in range(v3):
                if a1[v7][v8] in 'XS':
                    continue
                v9 = -1
                v10 = 0
                for v11, v12 in [(0, -1), (-1, 0), (-1, -1)]:
                    v13, v14 = (v7 + v11, v8 + v12)
                    if 0 <= v13 < v2 and 0 <= v14 < v3 and (v4[v13][v14][1] > 0):
                        v15 = v4[v13][v14][0]
                        if v15 > v9:
                            v9 = v15
                            v10 = v4[v13][v14][1]
                        elif v15 == v9:
                            v10 = (v10 + v4[v13][v14][1]) % v1
                if v9 != -1:
                    v16 = 0 if a1[v7][v8] == 'E' else int(a1[v7][v8])
                    v4[v7][v8] = [v9 + v16, v10]
        return v4[v2 - 1][v3 - 1]

class C1(object):

    def minimumSeconds(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 10 ** 9 + 7
        v4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v5 = [[v3] * v2 for v6 in range(v1)]
        v7 = []
        for v8 in range(v1):
            for v9 in range(v2):
                if a1[v8][v9] == '*':
                    v5[v8][v9] = 0
                    v7.append((v8, v9))
        while v7:
            v10 = []
            for v8, v9 in v7:
                for v11, v12 in v4:
                    v13, v14 = (v8 + v11, v9 + v12)
                    if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] != 'X') and (a1[v13][v14] != 'D') and (v5[v13][v14] == v3):
                        v5[v13][v14] = v5[v8][v9] + 1
                        v10.append((v13, v14))
            v7 = v10
        v15, v16 = (0, 0)
        for v8 in range(v1):
            for v9 in range(v2):
                if a1[v8][v9] == 'S':
                    v15, v16 = (v8, v9)
                    break
            else:
                continue
            break
        v17 = [[v3] * v2 for v6 in range(v1)]
        v18 = []
        if v5[v15][v16] > 0:
            v17[v15][v16] = 0
            v18.append((v15, v16))
        while v18:
            v19 = []
            for v8, v9 in v18:
                if a1[v8][v9] == 'D':
                    return v17[v8][v9]
                v20 = v17[v8][v9]
                for v11, v12 in v4:
                    v13, v14 = (v8 + v11, v9 + v12)
                    if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] != 'X') and (v17[v13][v14] == v3) and (v20 + 1 < v5[v13][v14]):
                        v17[v13][v14] = v20 + 1
                        v19.append((v13, v14))
            v18 = v19
        return -1

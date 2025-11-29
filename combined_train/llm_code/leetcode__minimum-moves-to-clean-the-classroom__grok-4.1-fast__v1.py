class C1(object):

    def minMoves(self, a1, a2):
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = len(a1)
        v3 = len(a1[0])
        v4 = v5 = None
        v6 = []
        for v7 in range(v2):
            for v8 in range(v3):
                v9 = a1[v7][v8]
                if v9 == 'S':
                    v4, v5 = (v7, v8)
                elif v9 == 'L':
                    v6.append((v7, v8))
        v10 = len(v6)
        v11 = (1 << v10) - 1
        v12 = [[-1] * v3 for v13 in range(v2)]
        for v14, (v15, v16) in enumerate(v6):
            v12[v15][v16] = v14
        v17 = [[[-1] * (1 << v10) for v13 in range(v3)] for v13 in range(v2)]
        v17[v4][v5][0] = a2
        v18 = [(v4, v5, 0, a2)]
        v19 = 0
        while v18:
            v20 = []
            for v21, v22, v23, v24 in v18:
                if v17[v21][v22][v23] != v24:
                    continue
                if v23 == v11:
                    return v19
                for v25, v26 in v1:
                    v27, v28 = (v21 + v25, v22 + v26)
                    v29 = v24 - 1
                    if not (0 <= v27 < v2 and 0 <= v28 < v3 and (a1[v27][v28] != 'X') and (v29 >= 0)):
                        continue
                    v30 = v23
                    if a1[v27][v28] == 'R':
                        v29 = a2
                    v14 = v12[v27][v28]
                    if v14 != -1:
                        v30 |= 1 << v14
                    if v29 > v17[v27][v28][v30]:
                        v17[v27][v28][v30] = v29
                        v20.append((v27, v28, v30, v29))
            v18 = v20
            v19 += 1
        return -1

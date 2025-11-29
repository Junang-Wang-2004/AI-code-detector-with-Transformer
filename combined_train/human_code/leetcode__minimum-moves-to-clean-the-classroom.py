class C1(object):

    def minMoves(self, a1, a2):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))
        v2, v3 = (len(a1), len(a1[0]))
        v4 = {}
        v5 = v6 = -1
        for v7 in range(v2):
            for v8 in range(len(a1[v7])):
                v9 = a1[v7][v8]
                if v9 == 'S':
                    v5, v6 = (v7, v8)
                elif v9 == 'L':
                    v4[v7, v8] = len(v4)
        v10 = [[[-1] * (1 << len(v4)) for v11 in range(v3)] for v11 in range(v2)]
        v10[v5][v6][0] = a2
        v12 = [(v5, v6, 0, a2)]
        v13 = 0
        while v12:
            v14 = []
            for v7, v8, v15, v16 in v12:
                if v10[v7][v8][v15] != v16:
                    continue
                if v15 == (1 << len(v4)) - 1:
                    return v13
                for v17, v18 in v1:
                    v19, v20 = (v7 + v17, v8 + v18)
                    v21 = v16 - 1
                    if not (0 <= v19 < v2 and 0 <= v20 < v3 and (a1[v19][v20] != 'X') and (v21 >= 0)):
                        continue
                    v22 = v15
                    if a1[v19][v20] == 'R':
                        v21 = a2
                    elif a1[v19][v20] == 'L':
                        v22 |= 1 << v4[v19, v20]
                    if v21 <= v10[v19][v20][v22]:
                        continue
                    v10[v19][v20][v22] = v21
                    v14.append((v19, v20, v22, v21))
            v12 = v14
            v13 += 1
        return -1

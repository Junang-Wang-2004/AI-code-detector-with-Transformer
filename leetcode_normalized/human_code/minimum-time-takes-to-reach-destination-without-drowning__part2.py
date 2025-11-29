class C1(object):

    def minimumSeconds(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))
        v2 = [[0 if a1[i][j] == '*' else -1 for v3 in range(len(a1[0]))] for v4 in range(len(a1))]
        v5 = [[-1] * len(a1[0]) for v6 in range(len(a1))]
        v7 = [(v4, v3) for v4 in range(len(a1)) for v3 in range(len(a1[0])) if a1[v4][v3] == '*']
        v8 = [next(((v4, v3) for v4 in range(len(a1)) for v3 in range(len(a1[0])) if a1[v4][v3] == 'S'))]
        v5[v8[0][0]][v8[0][1]] = 0
        while v7 or v8:
            v9, v10 = ([], [])
            for v4, v3 in v7:
                for v11, v12 in v1:
                    v13, v14 = (v4 + v11, v3 + v12)
                    if not (0 <= v13 < len(a1) and 0 <= v14 < len(a1[0]) and (a1[v13][v14] != 'X') and (a1[v13][v14] != 'D') and (v2[v13][v14] == -1)):
                        continue
                    v2[v13][v14] = 0
                    v9.append((v13, v14))
            for v4, v3 in v8:
                if a1[v4][v3] == 'D':
                    return v5[v4][v3]
                for v11, v12 in v1:
                    v13, v14 = (v4 + v11, v3 + v12)
                    if not (0 <= v13 < len(a1) and 0 <= v14 < len(a1[0]) and (a1[v13][v14] != 'X') and (v5[v13][v14] == v2[v13][v14] == -1)):
                        continue
                    v5[v13][v14] = v5[v4][v3] + 1
                    v10.append((v13, v14))
            v7, v8 = (v9, v10)
        return -1

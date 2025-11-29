class C1(object):

    def minimumSeconds(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))
        v2 = [[-1 if a1[i][j] == '*' else 0 for v3 in range(len(a1[0]))] for v4 in range(len(a1))]
        v5 = [(v4, v3, -1) for v4 in range(len(a1)) for v3 in range(len(a1[0])) if a1[v4][v3] == '*']
        v5.append(next(((v4, v3, 1) for v4 in range(len(a1)) for v3 in range(len(a1[0])) if a1[v4][v3] == 'S')))
        v2[v5[-1][0]][v5[-1][1]] = 1
        while v5:
            v6 = []
            for v4, v3, v7 in v5:
                if a1[v4][v3] == 'D':
                    return v7 - 1
                for v8, v9 in v1:
                    v10, v11 = (v4 + v8, v3 + v9)
                    if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (a1[v10][v11] != 'X') and (v2[v10][v11] != -1)):
                        continue
                    if v7 != -1 and v2[v10][v11] == 0:
                        v2[v10][v11] = 1
                        v6.append((v10, v11, v7 + 1))
                    elif v7 == -1 and a1[v10][v11] != 'D':
                        v2[v10][v11] = -1
                        v6.append((v10, v11, -1))
            v5 = v6
        return -1

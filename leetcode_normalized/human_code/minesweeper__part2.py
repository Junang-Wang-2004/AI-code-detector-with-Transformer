class C1(object):

    def updateBoard(self, a1, a2):
        """
        """
        if a1[a2[0]][a2[1]] == 'M':
            a1[a2[0]][a2[1]] = 'X'
            return a1
        v1 = [a2]
        while v1:
            v2 = []
            for v3, v4 in v1:
                v5 = 0
                v6 = []
                for v7 in range(-1, 2):
                    for v8 in range(-1, 2):
                        if v7 == v8 == 0:
                            continue
                        v9, v10 = (v3 + v7, v4 + v8)
                        if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[v3])):
                            continue
                        if a1[v9][v10] == 'M':
                            v5 += 1
                        elif a1[v9][v10] == 'E':
                            v6.append((v9, v10))
                if v5:
                    a1[v3][v4] = chr(v5 + ord('0'))
                    continue
                a1[v3][v4] = 'B'
                for v9, v10 in v6:
                    a1[v9][v10] = ' '
                    v2.append((v9, v10))
            v1 = v2
        return a1

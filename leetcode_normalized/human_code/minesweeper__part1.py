class C1(object):

    def updateBoard(self, a1, a2):
        """
        """
        if a1[a2[0]][a2[1]] == 'M':
            a1[a2[0]][a2[1]] = 'X'
            return a1
        v1 = [a2]
        while v1:
            v2, v3 = v1.pop()
            v4 = 0
            v5 = []
            for v6 in range(-1, 2):
                for v7 in range(-1, 2):
                    if v6 == v7 == 0:
                        continue
                    v8, v9 = (v2 + v6, v3 + v7)
                    if not (0 <= v8 < len(a1) and 0 <= v9 < len(a1[v2])):
                        continue
                    if a1[v8][v9] == 'M':
                        v4 += 1
                    elif a1[v8][v9] == 'E':
                        v5.append((v8, v9))
            if v4:
                a1[v2][v3] = chr(v4 + ord('0'))
                continue
            a1[v2][v3] = 'B'
            for v8, v9 in v5:
                a1[v8][v9] = ' '
                v1.append((v8, v9))
        return a1

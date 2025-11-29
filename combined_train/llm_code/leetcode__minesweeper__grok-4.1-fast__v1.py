class C1:

    def updateBoard(self, a1, a2):

        def reveal(a1, a2):
            v1 = 0
            for v2 in (-1, 0, 1):
                for v3 in (-1, 0, 1):
                    if v2 == 0 and v3 == 0:
                        continue
                    v4, v5 = (a1 + v2, a2 + v3)
                    if 0 <= v4 < len(a1) and 0 <= v5 < len(a1[0]) and (a1[v4][v5] == 'M'):
                        v1 += 1
            if v1 > 0:
                a1[a1][a2] = str(v1)
                return
            a1[a1][a2] = 'B'
            for v2 in (-1, 0, 1):
                for v3 in (-1, 0, 1):
                    if v2 == 0 and v3 == 0:
                        continue
                    v4, v5 = (a1 + v2, a2 + v3)
                    if 0 <= v4 < len(a1) and 0 <= v5 < len(a1[0]) and (a1[v4][v5] == 'E'):
                        reveal(v4, v5)
        v1, v2 = a2
        if a1[v1][v2] == 'M':
            a1[v1][v2] = 'X'
        else:
            reveal(v1, v2)
        return a1

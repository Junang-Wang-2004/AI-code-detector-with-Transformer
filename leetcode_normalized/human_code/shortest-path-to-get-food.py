class C1(object):

    def getFood(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = []
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4] == '*':
                    v2.append((v3, v4))
                    break
        v5 = 0
        while v2:
            v5 += 1
            v6 = []
            for v3, v4 in v2:
                for v7, v8 in v1:
                    v9, v10 = (v3 + v7, v4 + v8)
                    if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[0]) and (a1[v9][v10] != 'X')):
                        continue
                    if a1[v9][v10] == '#':
                        return v5
                    a1[v9][v10] = 'X'
                    v6.append((v9, v10))
            v2 = v6
        return -1

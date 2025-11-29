class C1:

    def checkValidGrid(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        if a1[0][0] != 0:
            return False
        v3 = v1 * v2
        v4, v5 = (0, 0)
        for v6 in range(1, v3):
            v7 = False
            for v8 in range(v1):
                for v9 in range(v2):
                    if a1[v8][v9] == v6:
                        v10 = abs(v8 - v4)
                        v11 = abs(v9 - v5)
                        if sorted([v10, v11]) == [1, 2]:
                            v4, v5 = (v8, v9)
                            v7 = True
                        break
                if v7:
                    break
            if not v7:
                return False
        return True

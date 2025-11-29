class C1(object):

    def minimumMoves(self, a1):
        v1 = len(a1)
        v2 = set()
        v3 = [(0, 0, 0)]
        v2.add((0, 0, 0))
        v4 = 0
        while v3:
            v5 = []
            for v6, v7, v8 in v3:
                if v6 == v1 - 1 and v7 == v1 - 2 and (v8 == 0):
                    return v4
                if v8 == 0:
                    if v7 + 2 < v1 and a1[v6][v7 + 2] == 0:
                        v9 = (v6, v7 + 1, 0)
                        if v9 not in v2:
                            v2.add(v9)
                            v5.append(v9)
                    if v6 + 1 < v1 and a1[v6 + 1][v7] == 0 and (a1[v6 + 1][v7 + 1] == 0):
                        v10 = (v6 + 1, v7, 0)
                        if v10 not in v2:
                            v2.add(v10)
                            v5.append(v10)
                        v11 = (v6, v7, 1)
                        if v11 not in v2:
                            v2.add(v11)
                            v5.append(v11)
                else:
                    if v6 + 2 < v1 and a1[v6 + 2][v7] == 0:
                        v9 = (v6 + 1, v7, 1)
                        if v9 not in v2:
                            v2.add(v9)
                            v5.append(v9)
                    if v7 + 1 < v1 and a1[v6][v7 + 1] == 0 and (a1[v6 + 1][v7 + 1] == 0):
                        v10 = (v6, v7 + 1, 1)
                        if v10 not in v2:
                            v2.add(v10)
                            v5.append(v10)
                        v11 = (v6, v7, 0)
                        if v11 not in v2:
                            v2.add(v11)
                            v5.append(v11)
            v3 = v5
            v4 += 1
        return -1

class C1(object):

    def minimumMoves(self, a1):
        """
        """
        v1, v2, v3 = (0, [(0, 0, False)], set())
        while v2:
            v4 = []
            for v5, v6, v7 in v2:
                if (v5, v6, v7) in v3:
                    continue
                if (v5, v6, v7) == (len(a1) - 1, len(a1) - 2, False):
                    return v1
                v3.add((v5, v6, v7))
                if not v7:
                    if v6 + 2 != len(a1[0]) and a1[v5][v6 + 2] == 0:
                        v4.append((v5, v6 + 1, v7))
                    if v5 + 1 != len(a1) and a1[v5 + 1][v6] == 0 and (a1[v5 + 1][v6 + 1] == 0):
                        v4.append((v5 + 1, v6, v7))
                        v4.append((v5, v6, not v7))
                else:
                    if v5 + 2 != len(a1) and a1[v5 + 2][v6] == 0:
                        v4.append((v5 + 1, v6, v7))
                    if v6 + 1 != len(a1) and a1[v5][v6 + 1] == 0 and (a1[v5 + 1][v6 + 1] == 0):
                        v4.append((v5, v6 + 1, v7))
                        v4.append((v5, v6, not v7))
            v2 = v4
            v1 += 1
        return -1

class C1(object):

    def highestPeak(self, a1):
        """
        """
        v1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v2 = []
        for v3, v4 in enumerate(a1):
            for v5, v6 in enumerate(v4):
                v4[v5] -= 1
                if not v6:
                    continue
                v2.append((v3, v5))
        while v2:
            v7 = []
            for v3, v5 in v2:
                for v8, v9 in v1:
                    v10, v11 = (v3 + v8, v5 + v9)
                    if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (a1[v10][v11] == -1)):
                        continue
                    a1[v10][v11] = a1[v3][v5] + 1
                    v2.append((v10, v11))
            v2 = v7
        return a1

class C1(object):

    def highestPeak(self, a1):
        """
        """
        v1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        v2, v3 = ([], [[-1] * len(a1[0]) for v4 in range(len(a1))])
        for v5, v6 in enumerate(a1):
            for v7, v8 in enumerate(v6):
                if not v8:
                    continue
                v3[v5][v7] = 0
                v2.append((v5, v7))
        while v2:
            v9 = []
            for v5, v7 in v2:
                for v10, v11 in v1:
                    v12, v13 = (v5 + v10, v7 + v11)
                    if not (0 <= v12 < len(a1) and 0 <= v13 < len(a1[0]) and (v3[v12][v13] == -1)):
                        continue
                    v3[v12][v13] = v3[v5][v7] + 1
                    v2.append((v12, v13))
            v2 = v9
        return v3

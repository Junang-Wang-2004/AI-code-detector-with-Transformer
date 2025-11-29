class C1(object):

    def nearestExit(self, a1, a2):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = ' '
        a2 = tuple(a2)
        v4 = set([a2])
        v5 = set([(r, 0) for v6 in range(len(a1) - 1) if a1[v6][0] == '.' and (v6, 0) != a2] + [(len(a1) - 1, c) for v7 in range(len(a1[0]) - 1) if a1[len(a1) - 1][v7] == '.' and (len(a1) - 1, v7) != a2] + [(v6, len(a1[0]) - 1) for v6 in reversed(range(1, len(a1))) if a1[v6][len(a1[0]) - 1] == '.' and (v6, len(a1[0]) - 1) != a2] + [(0, v7) for v7 in reversed(range(1, len(a1[0]))) if a1[0][v7] == '.' and (0, v7) != a2])
        v8 = 0
        while v4:
            for v6, v7 in v4:
                a1[v6][v7] = v2
            v9 = set()
            for v6, v7 in v4:
                if (v6, v7) in v5:
                    return v8
                for v10, v11 in v1:
                    v12, v13 = (v6 + v10, v7 + v11)
                    if not (0 <= v12 < len(a1) and 0 <= v13 < len(a1[0]) and (a1[v12][v13] == '.')):
                        continue
                    v9.add((v12, v13))
            v4 = v9
            v8 += 1
            if len(v4) > len(v5):
                v4, v5 = (v5, v4)
        return -1

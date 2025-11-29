class C1(object):

    def nearestExit(self, a1, a2):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = ' '
        a2 = tuple(a2)
        a1[a2[0]][a2[1]] = v2
        v4 = [(a2, 0)]
        while v4:
            v5 = []
            for (v6, v7), v8 in v4:
                if (v6, v7) != a2 and (v6 in (0, len(a1) - 1) or v7 in (0, len(a1[0]) - 1)):
                    return v8
                for v9, v10 in v1:
                    v11, v12 = (v6 + v9, v7 + v10)
                    if not (0 <= v11 < len(a1) and 0 <= v12 < len(a1[0]) and (a1[v11][v12] == '.')):
                        continue
                    a1[v11][v12] = v2
                    v4.append(((v11, v12), v8 + 1))
            v4 = v5
        return -1

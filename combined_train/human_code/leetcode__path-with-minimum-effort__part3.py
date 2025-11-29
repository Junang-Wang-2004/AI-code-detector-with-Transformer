class C1(object):

    def minimumEffortPath(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def check(a1, a2):
            v1 = [[False] * len(a1[0]) for v2 in range(len(a1))]
            v3, v4 = ({(0, 0)}, {(len(a1) - 1, len(a1[0]) - 1)})
            while v3:
                for v5, v6 in v3:
                    v1[v5][v6] = True
                v7 = set()
                for v5, v6 in v3:
                    if (v5, v6) in v4:
                        return True
                    for v8, v9 in v1:
                        v10, v11 = (v5 + v8, v6 + v9)
                        if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (abs(a1[v10][v11] - a1[v5][v6]) <= a2) and (not v1[v10][v11])):
                            continue
                        v7.add((v10, v11))
                v3 = v7
                if len(v3) > len(v4):
                    v3, v4 = (v4, v3)
            return False
        v2, v3 = (0, 10 ** 6)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(a1, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return v2

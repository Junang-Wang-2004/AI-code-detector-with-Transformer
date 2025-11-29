class C1(object):

    def robotSim(self, a1, a2):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2, v3, v4 = (0, 0, 0)
        v5 = set(map(tuple, a2))
        v6 = 0
        for v7 in a1:
            if v7 == -2:
                v4 = (v4 - 1) % 4
            elif v7 == -1:
                v4 = (v4 + 1) % 4
            else:
                for v8 in range(v7):
                    if (v2 + v1[v4][0], v3 + v1[v4][1]) not in v5:
                        v2 += v1[v4][0]
                        v3 += v1[v4][1]
                        v6 = max(v6, v2 * v2 + v3 * v3)
        return v6

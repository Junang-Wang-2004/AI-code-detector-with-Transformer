class C1(object):

    def countRoutes(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0] * (a4 + 1) for v3 in range(len(a1))]
        v2[a2][0] = 1
        for v4 in range(a4 + 1):
            for v5 in range(len(a1)):
                for v6 in range(len(a1)):
                    if v5 == v6:
                        continue
                    v7 = abs(a1[v5] - a1[v6])
                    if v4 - v7 < 0:
                        continue
                    v2[v5][v4] = (v2[v5][v4] + v2[v6][v4 - v7]) % v1
        return reduce(lambda x, y: (x + y) % v1, v2[a3])

class C1(object):

    def countRoutes(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [[0] * (a4 + 1) for v4 in range(v2)]
        v3[a2][0] = 1
        for v5 in range(a4 + 1):
            for v6 in range(v2):
                for v7 in range(v2):
                    if v6 == v7:
                        continue
                    v8 = abs(a1[v6] - a1[v7])
                    v9 = v5 + v8
                    if v9 <= a4:
                        v3[v7][v9] = (v3[v7][v9] + v3[v6][v5]) % v1
        v10 = 0
        for v11 in range(a4 + 1):
            v10 = (v10 + v3[a3][v11]) % v1
        return v10

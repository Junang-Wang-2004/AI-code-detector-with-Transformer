class C1(object):

    def countPaths(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v3 = [[0] * len(a1[0]) for v4 in range(len(a1))]
        v5 = []
        for v6 in range(len(a1)):
            for v7 in range(len(a1[0])):
                for v8, v9 in v2:
                    v10, v11 = (v6 + v8, v7 + v9)
                    if 0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (a1[v6][v7] > a1[v10][v11]):
                        v3[v6][v7] += 1
                if not v3[v6][v7]:
                    v5.append((v6, v7))
        v12 = [[1] * len(a1[0]) for v4 in range(len(a1))]
        v13 = 0
        while v5:
            v14 = []
            for v6, v7 in v5:
                v13 = (v13 + v12[v6][v7]) % v1
                for v8, v9 in v2:
                    v10, v11 = (v6 + v8, v7 + v9)
                    if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (a1[v6][v7] < a1[v10][v11])):
                        continue
                    v12[v10][v11] = (v12[v10][v11] + v12[v6][v7]) % v1
                    v3[v10][v11] -= 1
                    if not v3[v10][v11]:
                        v14.append((v10, v11))
            v5 = v14
        return v13

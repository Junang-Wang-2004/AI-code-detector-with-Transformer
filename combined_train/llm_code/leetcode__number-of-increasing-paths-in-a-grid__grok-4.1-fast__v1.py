class C1:

    def countPaths(self, a1):
        v1 = 10 ** 9 + 7
        v2 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not a1 or not a1[0]:
            return 0
        v3, v4 = (len(a1), len(a1[0]))
        v5 = [(a1[x][y], x, y) for v6 in range(v3) for v7 in range(v4)]
        v5.sort()
        v8 = [[1] * v4 for v9 in range(v3)]
        for v9, v6, v7 in v5:
            for v10, v11 in v2:
                v12, v13 = (v6 + v10, v7 + v11)
                if 0 <= v12 < v3 and 0 <= v13 < v4 and (a1[v6][v7] < a1[v12][v13]):
                    v8[v12][v13] = (v8[v12][v13] + v8[v6][v7]) % v1
        v14 = 0
        for v15 in range(v3):
            for v16 in range(v4):
                v14 = (v14 + v8[v15][v16]) % v1
        return v14

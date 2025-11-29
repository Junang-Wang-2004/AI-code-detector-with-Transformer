class C1:

    def imageSmoother(self, a1):
        if not a1 or not a1[0]:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]
        v5 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
        for v6 in range(v1):
            for v7 in range(v2):
                v8 = 0
                v9 = 0
                for v10, v11 in v5:
                    v12, v13 = (v6 + v10, v7 + v11)
                    if 0 <= v12 < v1 and 0 <= v13 < v2:
                        v8 += a1[v12][v13]
                        v9 += 1
                v3[v6][v7] = v8 // v9
        return v3

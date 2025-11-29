class C1(object):

    def findPaths(self, a1, a2, a3, a4, a5):
        v1 = 10 ** 9 + 7
        v2 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v3 = [[0] * a2 for v4 in range(a1)]
        v3[a4][a5] = 1
        v5 = 0
        for v4 in range(a3):
            v6 = [[0] * a2 for v4 in range(a1)]
            for v7 in range(a1):
                for v8 in range(a2):
                    v9 = v3[v7][v8]
                    for v10, v11 in v2:
                        v12, v13 = (v7 + v10, v8 + v11)
                        if 0 <= v12 < a1 and 0 <= v13 < a2:
                            v6[v12][v13] = (v6[v12][v13] + v9) % v1
                        else:
                            v5 = (v5 + v9) % v1
            v3 = v6
        return v5

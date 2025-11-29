class C1(object):

    def maximalSquare(self, a1):
        if not a1:
            return 0
        v1, v2 = (0, 1)
        v3 = [[[0, 0] for v4 in range(len(a1[0]))] for v5 in range(len(a1))]
        for v5 in reversed(range(len(a1))):
            for v4 in reversed(range(len(a1[v5]))):
                if a1[v5][v4] == '1':
                    v6, v7 = (1, 1)
                    if v5 + 1 < len(a1):
                        v6 = v3[v5 + 1][v4][v1] + 1
                    if v4 + 1 < len(a1[v5]):
                        v7 = v3[v5][v4 + 1][v2] + 1
                    v3[v5][v4] = [v6, v7]
        v8 = [[0 for v4 in range(len(a1[0]))] for v5 in range(len(a1))]
        v9 = 0
        for v5 in reversed(range(len(a1))):
            for v4 in reversed(range(len(a1[v5]))):
                v10 = min(v3[v5][v4][v1], v3[v5][v4][v2])
                if a1[v5][v4] == '1':
                    if v5 + 1 < len(a1) and v4 + 1 < len(a1[v5 + 1]):
                        v10 = min(v8[v5 + 1][v4 + 1] + 1, v10)
                    v8[v5][v4] = v10
                    v9 = max(v9, v10 * v10)
        return v9

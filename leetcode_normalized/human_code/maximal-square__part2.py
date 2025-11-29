class C1(object):

    def maximalSquare(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0 for v4 in range(v2)] for v5 in range(v1)]
        v6 = 0
        for v4 in range(v2):
            if a1[0][v4] == '1':
                v3[0][v4] = 1
            v6 = max(v6, v3[0][v4])
        for v5 in range(1, v1):
            if a1[v5][0] == '1':
                v3[v5][0] = 1
            else:
                v3[v5][0] = 0
            for v4 in range(1, v2):
                if a1[v5][v4] == '1':
                    v3[v5][v4] = min(v3[v5][v4 - 1], v3[v5 - 1][v4], v3[v5 - 1][v4 - 1]) + 1
                    v6 = max(v6, v3[v5][v4])
                else:
                    v3[v5][v4] = 0
        return v6 * v6

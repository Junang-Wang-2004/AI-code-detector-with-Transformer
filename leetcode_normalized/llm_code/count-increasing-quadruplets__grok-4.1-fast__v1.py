class C1(object):

    def countQuadruplets(self, a1):
        v1 = len(a1)
        v2 = [[0] * (v1 + 1) for v3 in range(v1)]
        for v4 in range(v1):
            v5 = 0
            for v6 in range(v4):
                v5 += a1[v6] < a1[v4]
                v2[v4][v6 + 1] = v5
        v7 = [[0] * (v1 + 1) for v3 in range(v1)]
        for v8 in range(v1):
            v5 = 0
            for v9 in range(v1 - 1, v8, -1):
                v5 += a1[v9] > a1[v8]
                v7[v8][v9] = v5
        v10 = 0
        for v4 in range(v1):
            for v8 in range(v4):
                if a1[v4] < a1[v8]:
                    v10 += v2[v4][v8] * v7[v8][v4 + 1]
        return v10

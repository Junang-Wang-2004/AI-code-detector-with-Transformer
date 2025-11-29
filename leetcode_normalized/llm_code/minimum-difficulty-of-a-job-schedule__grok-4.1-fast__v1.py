class C1(object):

    def minDifficulty(self, a1, a2):
        v1 = len(a1)
        if v1 < a2:
            return -1
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            v5 = 0
            for v6 in range(v4, v1):
                v5 = max(v5, a1[v6])
                v2[v4][v6] = v5
        v7 = [[float('inf')] * v1 for v3 in range(a2)]
        for v8 in range(v1):
            v7[0][v8] = v2[0][v8]
        for v9 in range(1, a2):
            for v8 in range(v9, v1):
                for v10 in range(v9 - 1, v8):
                    v11 = v7[v9 - 1][v10] + v2[v10 + 1][v8]
                    if v11 < v7[v9][v8]:
                        v7[v9][v8] = v11
        return v7[a2 - 1][v1 - 1]

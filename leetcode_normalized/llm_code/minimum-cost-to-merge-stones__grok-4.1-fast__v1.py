class C1:

    def mergeStones(self, a1, a2):
        v1 = len(a1)
        if (v1 - 1) % (a2 - 1):
            return -1
        v2 = [0] * (v1 + 1)
        for v3 in range(v1):
            v2[v3 + 1] = v2[v3] + a1[v3]
        v4 = [[0] * v1 for v5 in range(v1)]
        v6 = a2 - 1
        for v7 in range(v6, v1):
            for v8 in range(v1 - v7):
                v9 = v8 + v7
                v10 = float('inf')
                v11 = v8
                while v11 < v9:
                    v10 = min(v10, v4[v8][v11] + v4[v11 + 1][v9])
                    v11 += v6
                v4[v8][v9] = v10
                if v7 % v6 == 0:
                    v4[v8][v9] += v2[v9 + 1] - v2[v8]
        return v4[0][v1 - 1]

class C1:

    def maximumScore(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [0] * (v1 + 1)
        for v4 in range(v1):
            v3[v4 + 1] = v3[v4] + a1[v4][0]
        v5 = [0] * (v1 + 1)
        v6 = [0] * (v1 + 1)
        for v7 in range(1, v2):
            v8 = [0] * (v1 + 1)
            for v4 in range(v1):
                v8[v4 + 1] = v8[v4] + a1[v4][v7]
            v9 = max(v6)
            v10 = float('-inf')
            v11 = [0] * (v1 + 1)
            for v12 in range(v1 + 1):
                v10 = max(v10, v5[v12] - v3[v12])
                v11[v12] = v3[v12] + v10
                v11[v12] = max(v11[v12], v9)
            v13 = [float('-inf')] * (v1 + 2)
            for v14 in range(v1, -1, -1):
                v13[v14] = max(v13[v14 + 1], v6[v14] + v8[v14])
            v15 = [0] * (v1 + 1)
            for v12 in range(v1 + 1):
                v15[v12] = v13[v12 + 1] - v8[v12]
                v15[v12] = max(v15[v12], v11[v12])
            v5 = v11
            v6 = v15
            v3 = v8
        return max(v6)

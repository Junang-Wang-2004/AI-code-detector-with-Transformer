class C1:

    def getDistances(self, a1):
        v1 = {}
        for v2, v3 in enumerate(a1):
            if v3 not in v1:
                v1[v3] = []
            v1[v3].append(v2)
        v4 = [0] * len(a1)
        for v5 in v1.values():
            v6 = len(v5)
            v7 = [0] * (v6 + 1)
            for v8 in range(v6):
                v7[v8 + 1] = v7[v8] + v5[v8]
            v9 = [0] * (v6 + 1)
            v9[v6] = 0
            for v8 in range(v6 - 1, -1, -1):
                v9[v8] = v5[v8] + v9[v8 + 1]
            for v8 in range(v6):
                v10 = v5[v8]
                v11 = v8 * v10 - v7[v8]
                v12 = v9[v8 + 1] - (v6 - v8 - 1) * v10
                v4[v10] = v11 + v12
        return v4

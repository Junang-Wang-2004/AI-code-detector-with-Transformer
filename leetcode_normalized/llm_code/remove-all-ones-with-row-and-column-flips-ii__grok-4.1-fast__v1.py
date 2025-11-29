class C1:

    def removeOnes(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 * v2
        v4 = 0
        v5 = [0] * v1
        v6 = [0] * v2
        for v7 in range(v1):
            for v8 in range(v2):
                if a1[v7][v8]:
                    v9 = v7 * v2 + v8
                    v10 = 1 << v9
                    v4 |= v10
                    v5[v7] |= v10
                    v6[v8] |= v10
        if v4 == 0:
            return 0
        v11 = []
        for v7 in range(v1):
            for v8 in range(v2):
                if a1[v7][v8]:
                    v11.append(v5[v7] | v6[v8])
        v12 = float('inf')
        v13 = [v12] * (v4 + 1)
        v13[0] = 0
        for v14 in range(v4 + 1):
            if v13[v14] == v12:
                continue
            for v15 in v11:
                v16 = v14 | v15
                v13[v16] = min(v13[v16], v13[v14] + 1)
        return v13[v4]

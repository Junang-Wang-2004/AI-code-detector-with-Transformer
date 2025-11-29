class C1:

    def maxCompatibilitySum(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = len(a1[0])
        v4 = []
        for v5 in a1:
            v6 = []
            for v7 in a2:
                v8 = sum((1 for v9, v10 in zip(v5, v7) if v9 == v10))
                v6.append(v8)
            v4.append(v6)
        v11 = 1 << v2
        v12 = [-1] * v11
        v12[0] = 0
        for v13 in range(v1):
            v14 = [-1] * v11
            for v15 in range(v11):
                if v12[v15] == -1:
                    continue
                v14[v15] = max(v14[v15], v12[v15])
                for v16 in range(v2):
                    if v15 & 1 << v16 == 0:
                        v17 = v15 | 1 << v16
                        v18 = v12[v15] + v4[v13][v16]
                        v14[v17] = max(v14[v17], v18)
            v12 = v14
        v19 = 0
        for v20 in v12:
            if v20 > v19:
                v19 = v20
        return v19

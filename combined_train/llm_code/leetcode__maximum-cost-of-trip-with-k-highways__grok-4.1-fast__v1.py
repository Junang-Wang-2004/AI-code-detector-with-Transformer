class C1:

    def maximumCost(self, a1, a2, a3):
        if a3 + 1 > a1:
            return -1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = float('-inf')
        v7 = [[v6] * a1 for v2 in range(1 << a1)]
        for v8 in range(a1):
            v7[1 << v8][v8] = 0
        v9 = -1
        for v10 in range(1 << a1):
            v11 = bin(v10).count('1')
            for v12 in range(a1):
                if v10 & 1 << v12 == 0:
                    continue
                v13 = v7[v10][v12]
                if v13 == v6:
                    continue
                if v11 == a3 + 1:
                    v9 = max(v9, v13)
                    continue
                for v14, v15 in v1[v12]:
                    if v10 & 1 << v14 == 0:
                        v16 = v10 | 1 << v14
                        v7[v16][v14] = max(v7[v16][v14], v13 + v15)
        return v9

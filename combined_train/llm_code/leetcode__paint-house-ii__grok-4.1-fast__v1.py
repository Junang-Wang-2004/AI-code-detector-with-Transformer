class C1:

    def minCostII(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = a1[0][:]
        for v4 in range(1, v1):
            v5, v6 = (float('inf'), float('inf'))
            v7 = -1
            for v8 in range(v2):
                if v3[v8] < v5:
                    v6 = v5
                    v5 = v3[v8]
                    v7 = v8
                elif v3[v8] < v6:
                    v6 = v3[v8]
            v9 = [0] * v2
            for v8 in range(v2):
                v10 = v6 if v8 == v7 else v5
                v9[v8] = a1[v4][v8] + v10
            v3 = v9
        return min(v3)

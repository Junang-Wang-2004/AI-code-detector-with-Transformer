class C1:

    def minimumOperations(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [[0] * 10 for v4 in range(v2)]
        for v5 in range(v2):
            v6 = [0] * 10
            for v7 in range(v1):
                v6[a1[v7][v5]] += 1
            for v8 in range(10):
                v3[v5][v8] = v1 - v6[v8]
        v9 = [0] * 10
        for v5 in range(v2):
            v10 = [float('inf')] * 10
            for v11 in range(10):
                for v12 in range(10):
                    if v11 != v12:
                        v10[v12] = min(v10[v12], v9[v11] + v3[v5][v12])
            v9 = v10
        return min(v9)

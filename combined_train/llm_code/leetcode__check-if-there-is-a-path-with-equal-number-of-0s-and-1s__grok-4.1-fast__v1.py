class C1:

    def isThereAPath(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 + v2 - 1
        if v3 % 2 != 0:
            return False
        v4 = v3 // 2
        v5 = [float('inf')] * v2
        v5[0] = a1[0][0]
        for v6 in range(1, v2):
            v5[v6] = v5[v6 - 1] + a1[0][v6]
        for v7 in range(1, v1):
            v5[0] += a1[v7][0]
            for v6 in range(1, v2):
                v5[v6] = a1[v7][v6] + min(v5[v6], v5[v6 - 1])
        v8 = v5[-1]
        v9 = [float('-inf')] * v2
        v9[0] = a1[0][0]
        for v6 in range(1, v2):
            v9[v6] = v9[v6 - 1] + a1[0][v6]
        for v7 in range(1, v1):
            v9[0] += a1[v7][0]
            for v6 in range(1, v2):
                v9[v6] = a1[v7][v6] + max(v9[v6], v9[v6 - 1])
        v10 = v9[-1]
        return v8 <= v4 <= v10

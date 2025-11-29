class C1:

    def findTheCity(self, a1, a2, a3):
        v1 = [[float('inf')] * a1 for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3][v4] = v1[v4][v3] = v5
        for v6 in range(a1):
            v1[v6][v6] = 0
        for v7 in range(a1):
            for v6 in range(a1):
                for v8 in range(a1):
                    if v1[v6][v7] + v1[v7][v8] < v1[v6][v8]:
                        v1[v6][v8] = v1[v6][v7] + v1[v7][v8]
        v9 = float('inf')
        v10 = -1
        for v11 in range(a1):
            v12 = sum((1 for v13 in v1[v11] if v13 <= a3))
            if v12 < v9:
                v9 = v12
                v10 = v11
            elif v12 == v9:
                v10 = v11
        return v10

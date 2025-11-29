class C1:

    def maxOperations(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = {a1[0] + a1[1], a1[0] + a1[-1], a1[-2] + a1[-1]}
        v3 = 0
        for v4 in v2:
            v5 = [[0] * v1 for v6 in range(v1)]
            for v7 in range(2, v1 + 1):
                for v8 in range(v1 - v7 + 1):
                    v9 = v8 + v7 - 1
                    v10 = 0
                    if a1[v8] + a1[v8 + 1] == v4:
                        v10 = max(v10, 1 + (v5[v8 + 2][v9] if v8 + 2 <= v9 else 0))
                    if a1[v8] + a1[v9] == v4:
                        v10 = max(v10, 1 + (v5[v8 + 1][v9 - 1] if v8 + 1 <= v9 - 1 else 0))
                    if a1[v9 - 1] + a1[v9] == v4:
                        v10 = max(v10, 1 + (v5[v8][v9 - 2] if v8 <= v9 - 2 else 0))
                    v5[v8][v9] = v10
            v3 = max(v3, v5[0][v1 - 1])
        return v3

class C1:

    def maxCollectedFruits(self, a1):
        v1 = len(a1)
        for v2 in range(v1):
            v3 = v2 + 1
            v4 = v1 - v2 - 1
            if v3 < v4:
                for v5 in range(v3, v4):
                    a1[v2][v5] = 0
        for v2 in range(1, v1 - 1):
            for v5 in range(v2 + 1, v1):
                v6 = a1[v2 - 1][v5 - 1]
                v7 = a1[v2 - 1][v5]
                v8 = a1[v2 - 1][v5 + 1] if v5 + 1 < v1 else 0
                a1[v2][v5] += max(v6, v7, v8)
        for v5 in range(v1):
            v9 = v5 + 1
            v7 = v1 - v5 - 1
            if v9 < v7:
                for v2 in range(v9, v7):
                    a1[v2][v5] = 0
        for v5 in range(1, v1 - 1):
            for v2 in range(v5 + 1, v1):
                v6 = a1[v2 - 1][v5 - 1]
                v7 = a1[v2][v5 - 1]
                v8 = a1[v2 + 1][v5 - 1] if v2 + 1 < v1 else 0
                a1[v2][v5] += max(v6, v7, v8)
        v10 = sum((a1[k][k] for v11 in range(v1))) + a1[v1 - 2][v1 - 1] + a1[v1 - 1][v1 - 2]
        return v10

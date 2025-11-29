class C1:

    def maxScore(self, a1):
        v1 = 10 ** 18 + 5
        v2 = -v1
        v3 = len(a1)
        v4 = len(a1[0])
        for v5 in range(v3):
            for v6 in range(v4):
                v7 = a1[v5][v6 - 1] if v6 > 0 else v1
                v8 = a1[v5 - 1][v6] if v5 > 0 else v1
                v9 = min(v7, v8)
                v2 = max(v2, a1[v5][v6] - v9)
                a1[v5][v6] = min(a1[v5][v6], v9)
        return v2

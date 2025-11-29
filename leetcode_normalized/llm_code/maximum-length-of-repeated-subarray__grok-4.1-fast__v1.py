class C1:

    def findLength(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = 0
        v4 = [[0] * (v2 + 1) for v5 in range(v1 + 1)]
        for v6 in range(1, v1 + 1):
            for v7 in range(1, v2 + 1):
                if a1[v6 - 1] == a2[v7 - 1]:
                    v4[v6][v7] = v4[v6 - 1][v7 - 1] + 1
                    v3 = max(v3, v4[v6][v7])
        return v3

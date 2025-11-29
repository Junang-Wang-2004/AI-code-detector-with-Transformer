class C1:

    def minMoves2(self, a1):
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = v2 // 2
        v4 = v1[v3]
        v5 = 0
        for v6 in range(v3):
            v5 += v4 - v1[v6]
        for v6 in range(v3 + 1, v2):
            v5 += v1[v6] - v4
        return v5

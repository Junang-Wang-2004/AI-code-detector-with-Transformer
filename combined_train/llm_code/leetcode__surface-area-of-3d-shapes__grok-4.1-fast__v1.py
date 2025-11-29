class C1:

    def surfaceArea(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = 0
        for v5 in range(v1):
            for v6 in range(v1):
                v7 = a1[v5][v6]
                v4 += v7
                if v7 > 0:
                    v3 += 1
        v2 += 2 * v3 + 4 * v4
        for v5 in range(v1):
            for v6 in range(v1 - 1):
                v2 -= 2 * min(a1[v5][v6], a1[v5][v6 + 1])
        for v6 in range(v1):
            for v5 in range(v1 - 1):
                v2 -= 2 * min(a1[v5][v6], a1[v5 + 1][v6])
        return v2

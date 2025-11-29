class C1:

    def minCost(self, a1, a2, a3):
        a3[0][0] = a3[a1 - 1][a2 - 1] = 0
        a3[0][0] += 1
        for v1 in range(1, a2):
            a3[0][v1] += a3[0][v1 - 1] + 1 * (v1 + 1)
        for v2 in range(1, a1):
            a3[v2][0] += a3[v2 - 1][0] + (v2 + 1) * 1
        for v2 in range(1, a1):
            for v1 in range(1, a2):
                v3 = min(a3[v2 - 1][v1], a3[v2][v1 - 1])
                a3[v2][v1] += v3 + (v2 + 1) * (v1 + 1)
        return a3[a1 - 1][a2 - 1]

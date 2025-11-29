class C1:

    def numRollsToTarget(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        if a3 < a1 or a3 > a1 * a2:
            return 0
        v2 = [0] * (a3 + 1)
        v2[0] = 1
        for v3 in range(a1):
            v4 = [0] * (a3 + 2)
            for v5 in range(1, a3 + 2):
                v4[v5] = (v4[v5 - 1] + v2[v5 - 1]) % v1
            v6 = [0] * (a3 + 1)
            for v5 in range(1, a3 + 1):
                v7 = max(0, v5 - a2)
                v6[v5] = (v4[v5] - v4[v7] + v1) % v1
            v2 = v6
        return v2[a3]

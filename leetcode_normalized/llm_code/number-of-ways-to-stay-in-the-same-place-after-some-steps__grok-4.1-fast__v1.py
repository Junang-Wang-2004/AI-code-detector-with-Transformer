class C1:

    def numWays(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = min(a1 // 2 + 1, a2)
        v3 = [0] * v2
        v3[0] = 1
        for v4 in range(a1):
            v5 = [0] * v2
            for v6 in range(v2):
                v7 = v3[v6]
                if v6 > 0:
                    v7 = (v7 + v3[v6 - 1]) % v1
                if v6 + 1 < v2:
                    v7 = (v7 + v3[v6 + 1]) % v1
                v5[v6] = v7
            v3 = v5
        return v3[0]

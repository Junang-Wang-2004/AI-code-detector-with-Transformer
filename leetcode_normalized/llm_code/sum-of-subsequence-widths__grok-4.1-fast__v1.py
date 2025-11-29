class C1:

    def sumSubseqWidths(self, a1):
        v1 = 10 ** 9 + 7
        v2 = sorted(a1)
        v3 = len(v2)
        v4 = 1
        v5 = 0
        for v6 in range(v3):
            v5 = (v5 + v2[v6] * v4) % v1
            v4 = v4 * 2 % v1
        v4 = 1
        v7 = 0
        for v6 in range(v3 - 1, -1, -1):
            v7 = (v7 + v2[v6] * v4) % v1
            v4 = v4 * 2 % v1
        return (v5 - v7 + v1) % v1

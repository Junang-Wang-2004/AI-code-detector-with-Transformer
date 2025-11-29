class C1:

    def integerBreak(self, a1):
        v1 = [0] * (a1 + 1)
        for v2 in range(2, a1 + 1):
            for v3 in range(1, v2):
                v1[v2] = max(v1[v2], v3 * max(v2 - v3, v1[v2 - v3]))
        return v1[a1]

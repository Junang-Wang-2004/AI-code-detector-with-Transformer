class C1:

    def maxAbsValExpr(self, a1, a2):
        v1 = 0
        for v2 in (1, -1):
            for v3 in (1, -1):
                v4 = float('inf')
                for v5, v6, v7 in zip(range(len(a1)), a1, a2):
                    v8 = v2 * v6 + v3 * v7 + v5
                    v1 = max(v1, v8 - v4)
                    v4 = min(v4, v8)
        return v1

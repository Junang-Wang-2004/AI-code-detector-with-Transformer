class C1:

    def maxDotProduct(self, a1, a2):
        if len(a1) < len(a2):
            a1, a2 = (a2, a1)
        v3 = len(a1)
        v4 = len(a2)
        v5 = [0] * v4
        for v6 in range(v3):
            v7 = [0] * v4
            for v8 in range(v4):
                v9 = a1[v6] * a2[v8]
                v10 = 0
                if v6 > 0 and v8 > 0:
                    v10 = max(v5[v8 - 1], 0)
                v11 = v9 + v10
                v7[v8] = v11
                if v6 > 0:
                    v7[v8] = max(v7[v8], v5[v8])
                if v8 > 0:
                    v7[v8] = max(v7[v8], v7[v8 - 1])
            v5 = v7
        return v5[-1]

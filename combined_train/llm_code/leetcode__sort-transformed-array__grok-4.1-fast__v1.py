class C1:

    def sortTransformedArray(self, a1, a2, a3, a4):
        v1 = len(a1)
        if v1 == 0:
            return []

        def compute(a1):
            return a2 * a1 * a1 + a3 * a1 + a4
        v2 = [0] * v1
        v3, v4 = (0, v1 - 1)
        if a2 > 0:
            v5 = v1 - 1
            while v3 <= v4:
                v6 = compute(a1[v3])
                v7 = compute(a1[v4])
                if v6 > v7:
                    v2[v5] = v6
                    v3 += 1
                else:
                    v2[v5] = v7
                    v4 -= 1
                v5 -= 1
        else:
            v5 = 0
            while v3 <= v4:
                v6 = compute(a1[v3])
                v7 = compute(a1[v4])
                if v6 < v7:
                    v2[v5] = v6
                    v3 += 1
                else:
                    v2[v5] = v7
                    v4 -= 1
                v5 += 1
        return v2

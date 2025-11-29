class C1:

    def restoreMatrix(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = [[0] * v2 for v4 in range(v1)]
        v5 = 0
        while v5 < v1:
            v6 = 0
            while v6 < v2 and a1[v5] > 0:
                if a2[v6] > 0:
                    v7 = min(a1[v5], a2[v6])
                    v3[v5][v6] = v7
                    a1[v5] -= v7
                    a2[v6] -= v7
                v6 += 1
            v5 += 1
        return v3

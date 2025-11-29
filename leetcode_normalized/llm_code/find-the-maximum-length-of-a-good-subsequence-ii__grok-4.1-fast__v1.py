class C1:

    def maximumLength(self, a1, a2):
        v1 = [{} for v2 in range(a2 + 1)]
        v3 = [0] * (a2 + 1)
        for v4 in a1:
            v5 = v3[:]
            for v6 in range(a2 + 1):
                v7 = v1[v6].get(v4, 0) + 1
                if v6 > 0:
                    v7 = max(v7, v5[v6 - 1] + 1)
                v1[v6][v4] = v7
                v3[v6] = max(v3[v6], v7)
        return v3[a2]

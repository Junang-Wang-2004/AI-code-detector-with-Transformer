class C1:

    def countSubmatrices(self, a1, a2):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        for v4 in range(v2):
            v5 = v2 - v4
            v6 = 0
            for v7 in range(v1):
                if a1[v7][v4] <= a2:
                    v6 += 1
                    v3 += v6 * v5
                else:
                    v6 = 0
        return v3

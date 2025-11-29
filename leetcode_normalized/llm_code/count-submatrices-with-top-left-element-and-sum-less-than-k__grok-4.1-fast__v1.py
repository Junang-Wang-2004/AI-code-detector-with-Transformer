class C1:

    def countSubmatrices(self, a1, a2):
        v1 = len(a1)
        v2 = len(a1[0]) if a1 else 0
        for v3 in range(v1):
            for v4 in range(1, v2):
                a1[v3][v4] += a1[v3][v4 - 1]
        for v4 in range(v2):
            for v3 in range(1, v1):
                a1[v3][v4] += a1[v3 - 1][v4]
        v5 = 0
        for v3 in range(v1):
            for v4 in range(v2):
                if a1[v3][v4] <= a2:
                    v5 += 1
        return v5

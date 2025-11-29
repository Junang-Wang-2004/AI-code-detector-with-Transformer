class C1:

    def maximumPopulation(self, a1):
        v1 = 1950
        v2 = 2050
        v3 = -1
        v4 = v1
        for v5 in range(v1, v2 + 1):
            v6 = sum((b <= v5 < d for v7, v8 in a1))
            if v6 > v3:
                v3 = v6
                v4 = v5
        return v4

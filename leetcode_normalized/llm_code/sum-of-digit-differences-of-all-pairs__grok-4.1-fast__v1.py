class C1:

    def sumDigitDifferences(self, a1):
        v1 = len(a1)
        v2 = max((len(str(num)) for v3 in a1))
        v4 = [[0] * 10 for v5 in range(v2)]
        for v3 in a1:
            v6 = str(v3).zfill(v2)
            for v7, v8 in enumerate(v6):
                v4[v7][int(v8)] += 1
        v9 = 0
        for v10 in v4:
            v11 = sum((c * c for v12 in v10))
            v9 += (v1 * v1 - v11) // 2
        return v9

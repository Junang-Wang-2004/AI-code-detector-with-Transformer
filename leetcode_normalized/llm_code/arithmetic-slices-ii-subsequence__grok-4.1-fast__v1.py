class C1:

    def numberOfArithmeticSlices(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = [{} for v4 in range(v1)]
        for v5 in range(1, v1):
            for v6 in range(v5):
                v7 = a1[v5] - a1[v6]
                v8 = v3[v6].get(v7, 0)
                v9 = v3[v5].get(v7, 0) + v8 + 1
                v3[v5][v7] = v9
                v2 += v8
        return v2

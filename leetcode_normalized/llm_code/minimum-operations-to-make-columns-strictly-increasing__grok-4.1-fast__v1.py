class C1:

    def minimumOperations(self, a1):
        v1 = 0
        v2, v3 = (len(a1), len(a1[0]))
        for v4 in range(v3):
            v5 = a1[0][v4]
            for v6 in range(1, v2):
                v7 = a1[v6][v4]
                if v7 <= v5:
                    v8 = v5 + 1
                    v1 += v8 - v7
                    v5 = v8
                else:
                    v5 = v7
        return v1

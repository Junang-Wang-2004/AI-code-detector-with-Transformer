class C1:

    def spiralMatrixIII(self, a1, a2, a3, a4):
        v1 = [[a3, a4]]
        v2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v3, v4 = (a3, a4)
        v5 = 1
        v6 = 0
        v7 = a1 * a2
        while len(v1) < v7:
            for v8 in range(2):
                v9, v10 = v2[v6]
                for v8 in range(v5):
                    v3 += v9
                    v4 += v10
                    if 0 <= v3 < a1 and 0 <= v4 < a2:
                        v1.append([v3, v4])
                    if len(v1) == v7:
                        return v1
                v6 = (v6 + 1) % 4
            v5 += 1
        return v1

class C1:

    def numSpecial(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [sum(row) for v4 in a1]
        v5 = [sum((a1[r][c] for v6 in range(v1))) for v7 in range(v2)]
        v8 = 0
        for v9 in range(v1):
            for v10 in range(v2):
                if a1[v9][v10] and v3[v9] == 1 and (v5[v10] == 1):
                    v8 += 1
        return v8

class C1:

    def shiftGrid(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = v1 * v2
        a2 %= v3
        v5 = [a1[i][j] for v6 in range(v1) for v7 in range(v2)]
        v5 = v5[-a2:] + v5[:-a2]
        v8 = 0
        for v6 in range(v1):
            for v7 in range(v2):
                a1[v6][v7] = v5[v8]
                v8 += 1
        return a1

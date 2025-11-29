class C1:

    def oddCells(self, a1, a2, a3):
        v1 = {}
        v2 = {}
        for v3, v4 in a3:
            v1[v3] = v1.get(v3, 0) + 1
            v2[v4] = v2.get(v4, 0) + 1
        v5 = sum((val % 2 for v6 in v1.values()))
        v7 = sum((v6 % 2 for v6 in v2.values()))
        return v5 * a2 + v7 * a1 - 2 * v5 * v7

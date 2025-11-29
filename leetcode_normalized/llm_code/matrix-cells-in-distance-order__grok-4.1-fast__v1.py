class C1:

    def allCellsDistOrder(self, a1, a2, a3, a4):
        v1 = [[i, j] for v2 in range(a1) for v3 in range(a2)]
        v1.sort(key=lambda p: (abs(p[0] - a3) + abs(p[1] - a4), p[0], p[1]))
        return v1

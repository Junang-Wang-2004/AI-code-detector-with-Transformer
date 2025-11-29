class C1:

    def specialGrid(self, a1):
        v1 = 1 << a1
        v2 = [[0] * v1 for v3 in range(v1)]

        def fill(a1, a2, a3, a4):
            if a3 == 1:
                v2[a1][a2] = a4
                return a4 + 1
            v1 = a3 // 2
            a4 = fill(a1, a2 + v1, v1, a4)
            a4 = fill(a1 + v1, a2 + v1, v1, a4)
            a4 = fill(a1 + v1, a2, v1, a4)
            a4 = fill(a1, a2, v1, a4)
            return a4
        fill(0, 0, v1, 0)
        return v2

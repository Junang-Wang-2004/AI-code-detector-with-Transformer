class C1:

    def maxSideLength(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [[0] * (v2 + 1) for v4 in range(v1 + 1)]
        for v5 in range(v1):
            for v6 in range(v2):
                v3[v5 + 1][v6 + 1] = v3[v5 + 1][v6] + v3[v5][v6 + 1] - v3[v5][v6] + a1[v5][v6]

        def has_square(a1):
            for v1 in range(a1 - 1, v1):
                for v2 in range(a1 - 1, v2):
                    v3, v4 = (v1 - a1 + 1, v2 - a1 + 1)
                    v5 = v3[v1 + 1][v2 + 1] - v3[v1 + 1][v4] - v3[v3 + 1][v2 + 1] + v3[v3 + 1][v4]
                    if v5 <= a2:
                        return True
            return False
        v7 = 1
        v8 = min(v1, v2) + 1
        while v7 < v8:
            v9 = (v7 + v8) // 2
            if has_square(v9):
                v7 = v9 + 1
            else:
                v8 = v9
        return v7 - 1

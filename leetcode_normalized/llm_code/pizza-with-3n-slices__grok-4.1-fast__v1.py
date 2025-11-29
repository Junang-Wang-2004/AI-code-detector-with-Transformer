class C1:

    def maxSizeSlices(self, a1):
        v1 = len(a1)
        v2 = v1 // 3

        def max_non_adjacent(a1, a2):
            v1 = a2 - a1
            if v1 <= 0:
                return 0
            v2 = [[0] * (v2 + 1) for v3 in range(v1 + 1)]
            for v4 in range(1, v1 + 1):
                v5 = a1[a1 + v4 - 1]
                for v6 in range(v2 + 1):
                    v2[v4][v6] = v2[v4 - 1][v6]
                    if v6 > 0:
                        v7 = v2[v4 - 2][v6 - 1] if v4 >= 2 else 0
                        v2[v4][v6] = max(v2[v4][v6], v5 + v7)
            return v2[v1][v2]
        return max(max_non_adjacent(0, v1 - 1), max_non_adjacent(1, v1))

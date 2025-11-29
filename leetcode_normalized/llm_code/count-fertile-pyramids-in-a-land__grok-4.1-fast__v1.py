class C1:

    def countPyramids(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))

        def count_direction(a1):
            v1 = [0] * v2
            v2 = 0
            for v3 in range(1, v1):
                v4 = [0] * v2
                for v5 in range(1, v2 - 1):
                    if a1[v3][v5] == 1 and a1[v3 - 1][v5 - 1] == 1 and (a1[v3 - 1][v5] == 1) and (a1[v3 - 1][v5 + 1] == 1):
                        v4[v5] = min(v1[v5 - 1], v1[v5 + 1]) + 1
                v1 = v4
                v2 += sum(v1)
            return v2
        return count_direction(a1) + count_direction(a1[::-1])

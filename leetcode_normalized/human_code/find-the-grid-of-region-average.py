class C1(object):

    def resultGrid(self, a1, a2):
        """
        """

        def check(a1, a2):
            return all((abs(a1[ni][nj] - a1[ni + 1][nj]) <= a2 for v1 in range(a1 - 1, a1 + 1) for v2 in range(a2 - 1, a2 + 2))) and all((abs(a1[v1][v2] - a1[v1][v2 + 1]) <= a2 for v1 in range(a1 - 1, a1 + 2) for v2 in range(a2 - 1, a2 + 1)))
        v1 = [[0] * len(a1[0]) for v2 in range(len(a1))]
        v3 = [[0] * len(a1[0]) for v2 in range(len(a1))]
        for v4 in range(1, len(a1) - 1):
            for v5 in range(1, len(a1[0]) - 1):
                if not check(v4, v5):
                    continue
                v6 = sum((a1[ni][nj] for v7 in range(v4 - 1, v4 + 2) for v8 in range(v5 - 1, v5 + 2))) // 9
                for v7 in range(v4 - 1, v4 + 2):
                    for v8 in range(v5 - 1, v5 + 2):
                        v3[v7][v8] += 1
                        v1[v7][v8] += v6
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                if v3[v4][v5]:
                    v1[v4][v5] //= v3[v4][v5]
                else:
                    v1[v4][v5] = a1[v4][v5]
        return v1

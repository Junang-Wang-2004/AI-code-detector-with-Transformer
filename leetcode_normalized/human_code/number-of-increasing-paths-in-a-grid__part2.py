class C1(object):

    def countPaths(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def memoization(a1, a2, a3, a4):
            if not a4[a2][a3]:
                a4[a2][a3] = 1
                for v1, v2 in v2:
                    v3, v4 = (a2 + v1, a3 + v2)
                    if 0 <= v3 < len(a1) and 0 <= v4 < len(a1[0]) and (a1[a2][a3] < a1[v3][v4]):
                        a4[a2][a3] = (a4[a2][a3] + memoization(a1, v3, v4, a4)) % v1
            return a4[a2][a3]
        v3 = [[0] * len(a1[0]) for v4 in range(len(a1))]
        return sum((memoization(a1, i, j, v3) for v5 in range(len(a1)) for v6 in range(len(a1[0])))) % v1

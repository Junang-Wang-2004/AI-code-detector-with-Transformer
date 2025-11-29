class C1(object):

    def lenOfVDiagonal(self, a1):
        """
        """

        def memoization(a1, a2, a3, a4, a5):
            if not (0 <= a1 < n and 0 <= a2 < m):
                return 0
            if a1[a1][a2] != a3:
                return 0
            if lookup[a5][a3][a4][a1][a2] == 0:
                v1, v2 = (a1 + directions[a4][0], a2 + directions[a4][1])
                v3 = 0 if a3 == 2 else 2
                v4 = memoization(v1, v2, v3, a4, a5) + 1
                if a5 != 1:
                    v5 = (a4 + 1) % 4
                    v4 = max(v4, memoization(v1, v2, v3, v5, a5 + 1) + 1)
                lookup[a5][a3][a4][a1][a2] = v4
            return lookup[a5][a3][a4][a1][a2]
        v1, v2 = (len(a1), len(a1[0]))
        v3 = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        v4 = [[[[[0] * v2 for v5 in range(v1)] for v5 in range(4)] for v5 in range(3)] for v5 in range(2)]
        v6 = 0
        for v7 in range(v1):
            for v8 in range(v2):
                if a1[v7][v8] == 1:
                    for v9 in range(4):
                        v6 = max(v6, memoization(v7, v8, 1, v9, 0))
        return v6

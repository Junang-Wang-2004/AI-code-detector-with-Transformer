class C1(object):

    def minimumMoves(self, a1):
        """
        """

        def dist(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])

        def backtracking(a1):
            if a1 == len(zero):
                return 0
            v1 = float('inf')
            v2, v3 = zero[a1]
            for v4 in range(len(a1)):
                for v5 in range(len(a1[0])):
                    if not a1[v4][v5] >= 2:
                        continue
                    a1[v4][v5] -= 1
                    v1 = min(v1, dist((v2, v3), (v4, v5)) + backtracking(a1 + 1))
                    a1[v4][v5] += 1
            return v1
        v1 = [(i, j) for v2 in range(len(a1)) for v3 in range(len(a1[0])) if a1[v2][v3] == 0]
        return backtracking(0)

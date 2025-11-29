class C1(object):

    def numberOfSets(self, a1, a2, a3):
        """
        """

        def check(a1, a2):
            return all((a2[i][j] <= a2 for v1 in range(a1) if a1 & 1 << v1 for v2 in range(v1 + 1, a1) if a1 & 1 << v2))

        def floydWarshall(a1, a2):
            for v1 in range(len(a1)):
                for v2 in range(v1 + 1, len(a1[v1])):
                    a1[v2][v1] = a1[v1][v2] = min(a1[v1][v2], a1[v1][a2] + a1[a2][v2])

        def backtracking(a1, a2, a3):
            if a1 == a1:
                result[0] += check(a2, a3)
                return
            for v1 in range(2):
                v2 = [d[:] for v3 in a3]
                if v1:
                    floydWarshall(v2, a1)
                backtracking(a1 + 1, a2 | v1 << a1, v2)
        v1 = [[0 if u == v else float('inf') for v2 in range(a1)] for v3 in range(a1)]
        for v3, v2, v4 in a3:
            v1[v3][v2] = min(v1[v3][v2], v4)
            v1[v2][v3] = min(v1[v2][v3], v4)
        v5 = [0]
        backtracking(0, 0, [d[:] for v6 in v1])
        return v5[0]

class C1(object):

    def countSubIslands(self, a1, a2):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(a1, a2, a3, a4):
            if not (0 <= a3 < len(a2) and 0 <= a4 < len(a2[0]) and (a2[a3][a4] == 1)):
                return 1
            a2[a3][a4] = 0
            v1 = a1[a3][a4]
            for v2, v3 in v1:
                v1 &= dfs(a1, a2, a3 + v2, a4 + v3)
            return v1
        return sum((dfs(a1, a2, i, j) for v2 in range(len(a2)) for v3 in range(len(a2[0])) if a2[v2][v3]))

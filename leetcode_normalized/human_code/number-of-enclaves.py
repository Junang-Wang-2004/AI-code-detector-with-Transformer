class C1(object):

    def numEnclaves(self, a1):
        """
        """
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(a1, a2, a3):
            if not (0 <= a2 < len(a1) and 0 <= a3 < len(a1[0]) and a1[a2][a3]):
                return
            a1[a2][a3] = 0
            for v1 in v1:
                dfs(a1, a2 + v1[0], a3 + v1[1])
        for v2 in range(len(a1)):
            dfs(a1, v2, 0)
            dfs(a1, v2, len(a1[0]) - 1)
        for v3 in range(1, len(a1[0]) - 1):
            dfs(a1, 0, v3)
            dfs(a1, len(a1) - 1, v3)
        return sum((sum(row) for v4 in a1))

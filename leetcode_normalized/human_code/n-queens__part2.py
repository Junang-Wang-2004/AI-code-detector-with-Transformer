class C1(object):

    def solveNQueens(self, a1):
        """
        """

        def dfs(a1, a2, a3):
            v1 = len(a1)
            if v1 == a1:
                ress.append(a1)
            for v2 in range(a1):
                if v2 not in a1 and v1 - v2 not in a2 and (v1 + v2 not in a3):
                    dfs(a1 + [v2], a2 + [v1 - v2], a3 + [v1 + v2])
        v1 = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (a1 - i - 1) for v2 in res] for v3 in v1]

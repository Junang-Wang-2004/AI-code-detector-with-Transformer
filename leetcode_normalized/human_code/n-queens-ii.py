class C1(object):

    def totalNQueens(self, a1):
        """
        """

        def dfs(a1):
            if a1 == a1:
                return 1
            v1 = 0
            for v2 in range(a1):
                if cols[v2] or main_diag[a1 + v2] or anti_diag[a1 - v2 + (a1 - 1)]:
                    continue
                cols[v2] = main_diag[a1 + v2] = anti_diag[a1 - v2 + (a1 - 1)] = True
                v1 += dfs(a1 + 1)
                cols[v2] = main_diag[a1 + v2] = anti_diag[a1 - v2 + (a1 - 1)] = False
            return v1
        v1 = []
        v2, v3, v4 = ([False] * a1, [False] * (2 * a1 - 1), [False] * (2 * a1 - 1))
        return dfs(0)

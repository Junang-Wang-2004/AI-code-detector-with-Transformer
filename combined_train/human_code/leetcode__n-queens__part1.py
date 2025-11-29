class C1(object):

    def solveNQueens(self, a1):
        """
        """

        def dfs(a1):
            if a1 == a1:
                result.append(['.' * x + 'Q' + '.' * (a1 - x - 1) for v1 in curr])
                return
            for v2 in range(a1):
                if cols[v2] or main_diag[a1 + v2] or anti_diag[a1 - v2 + (a1 - 1)]:
                    continue
                cols[v2] = main_diag[a1 + v2] = anti_diag[a1 - v2 + (a1 - 1)] = True
                curr.append(v2)
                dfs(a1 + 1)
                curr.pop()
                cols[v2] = main_diag[a1 + v2] = anti_diag[a1 - v2 + (a1 - 1)] = False
        v1, v2 = ([], [])
        v3, v4, v5 = ([False] * a1, [False] * (2 * a1 - 1), [False] * (2 * a1 - 1))
        dfs(0)
        return v1

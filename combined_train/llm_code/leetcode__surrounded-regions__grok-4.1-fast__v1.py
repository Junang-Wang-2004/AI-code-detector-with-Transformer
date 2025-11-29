class C1:

    def solve(self, a1):
        if not a1 or not a1[0]:
            return
        v1, v2 = (len(a1), len(a1[0]))

        def dfs(a1, a2):
            if a1 < 0 or a1 >= v1 or a2 < 0 or (a2 >= v2) or (a1[a1][a2] != 'O'):
                return
            a1[a1][a2] = 'T'
            dfs(a1 + 1, a2)
            dfs(a1 - 1, a2)
            dfs(a1, a2 + 1)
            dfs(a1, a2 - 1)
        for v3 in range(v1):
            dfs(v3, 0)
            dfs(v3, v2 - 1)
        for v4 in range(v2):
            dfs(0, v4)
            dfs(v1 - 1, v4)
        for v3 in range(v1):
            for v4 in range(v2):
                a1[v3][v4] = 'X' if a1[v3][v4] == 'O' else 'O'

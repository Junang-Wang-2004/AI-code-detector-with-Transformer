class C1(object):

    def removeBoxes(self, a1):
        """
        """

        def dfs(a1, a2, a3, a4, a5):
            if a2 > a3:
                return 0
            if a5[a2][a3][a4]:
                return a5[a2][a3][a4]
            v1, v2 = (a2, a4)
            while a2 < a3 and a1[a2 + 1] == a1[a2]:
                a2 += 1
                a4 += 1
            v5 = dfs(a1, a2 + 1, a3, 0, a5) + (a4 + 1) ** 2
            for v6 in range(a2 + 1, a3 + 1):
                if a1[v6] == a1[a2]:
                    v5 = max(v5, dfs(a1, a2 + 1, v6 - 1, 0, a5) + dfs(a1, v6, a3, a4 + 1, a5))
            a5[v1][a3][v2] = v5
            return v5
        v1 = [[[0] * len(a1) for v2 in range(len(a1))] for v2 in range(len(a1))]
        return dfs(a1, 0, len(a1) - 1, 0, v1)

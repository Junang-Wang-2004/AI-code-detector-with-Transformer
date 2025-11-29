class C1(object):

    def lastMarkedNodes(self, a1):
        """
        """

        def increase(a1):
            return (a1[0] + 1, a1[1])

        def dfs1(a1, a2):
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                dfs1(v1, a1)
                v2 = increase(dp[v1][0])
                for v3 in range(len(dp[a1])):
                    if v2 > dp[a1][v3]:
                        v2, dp[a1][v3] = (dp[a1][v3], v2)

        def dfs2(a1, a2, a3):
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                dfs2(v1, a1, increase(max(dp[a1][dp[a1][0][1] == dp[v1][0][1]], a3)))
            result[a1] = max(dp[a1][0], a3)[1]
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [[(0, v3)] * 2 for v3 in range(len(v1))]
        dfs1(0, -1)
        v6 = [-1] * len(v1)
        dfs2(0, -1, (0, -1))
        return v6

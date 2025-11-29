class C1(object):

    def timeTaken(self, a1):
        """
        """

        def dfs1(a1, a2):
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                dfs1(v1, a1)
                v2 = [1 + int(v1 % 2 == 0) + dp[v1][0][0], v1]
                for v3 in range(len(dp[a1])):
                    if v2 > dp[a1][v3]:
                        v2, dp[a1][v3] = (dp[a1][v3], v2)

        def dfs2(a1, a2, a3):
            result[a1] = max(dp[a1][0][0], a3)
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                dfs2(v1, a1, 1 + int(a1 % 2 == 0) + max(dp[a1][0][0] if dp[a1][0][1] != v1 else dp[a1][1][0], a3))
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [[[0, -1] for v2 in range(2)] for v2 in range(len(a1) + 1)]
        dfs1(0, -1)
        v6 = [0] * (len(a1) + 1)
        dfs2(0, -1, 0)
        return v6

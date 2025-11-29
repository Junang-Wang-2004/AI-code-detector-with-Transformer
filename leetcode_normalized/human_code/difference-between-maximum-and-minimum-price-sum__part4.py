class C1(object):

    def maxOutput(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            dp[a1] = a3[a1]
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                dp[a1] = max(dp[a1], dfs(v1, a1) + a3[a1])
            return dp[a1]

        def dfs2(a1, a2, a3):
            result[0] = max(result[0], a3, dp[a1] - a3[a1])
            v1 = [[a3, a2], [0, -1]]
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                a3 = [dp[v2], v2]
                for v4 in range(len(v1)):
                    if a3 > v1[v4]:
                        v1[v4], a3 = (a3, v1[v4])
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                dfs2(v2, a1, (v1[0][0] if v1[0][1] != v2 else v1[1][0]) + a3[a1])
        v1 = [0]
        v2 = [0] * a1
        v3 = [[] for v4 in range(a1)]
        for v5, v6 in a2:
            v3[v5].append(v6)
            v3[v6].append(v5)
        dfs(0, -1)
        dfs2(0, -1, 0)
        return v1[0]

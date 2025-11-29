class C1(object):

    def subtreeInversionSum(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            dp.append([0] * 2)
            v1, v2, v3 = (a2[a1], 0, 0)
            for v4 in adj[a1]:
                if v4 == a2:
                    continue
                v5, v6, v7 = dfs(v4, a1)
                v1 += v5
                v2 += v6
                v3 += v7
            v2 = max(v2, dp[-1][1] - 2 * v1)
            v3 = max(v3, dp[-1][0] + 2 * v1)
            dp.pop()
            if len(dp) - a3 >= 0:
                dp[len(dp) - a3][0] += v2
                dp[len(dp) - a3][1] += v3
            return (v1, v2, v3)
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = []
        v6, v7, v8 = dfs(0, -1)
        return v6 + v7

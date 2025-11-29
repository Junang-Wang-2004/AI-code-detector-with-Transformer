class C1(object):

    def numOfWays(self, a1):
        """
        """

        def dfs(a1):
            if len(a1) <= 2:
                return 1
            v1 = [v for v2 in a1 if v2 < a1[0]]
            v3 = [v2 for v2 in a1 if v2 > a1[0]]
            v4 = dp[len(v1) + len(v3)][len(v1)]
            v4 = v4 * dfs(v1) % MOD
            v4 = v4 * dfs(v3) % MOD
            return v4
        return (dfs(a1) - 1) % MOD

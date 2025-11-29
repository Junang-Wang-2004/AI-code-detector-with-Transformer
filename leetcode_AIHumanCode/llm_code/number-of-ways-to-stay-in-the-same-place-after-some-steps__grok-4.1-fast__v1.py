class Solution:
    def numWays(self, steps, arrLen):
        MOD = 10**9 + 7
        max_pos = min(steps // 2 + 1, arrLen)
        dp = [0] * max_pos
        dp[0] = 1
        for _ in range(steps):
            new_dp = [0] * max_pos
            for i in range(max_pos):
                ways = dp[i]
                if i > 0:
                    ways = (ways + dp[i - 1]) % MOD
                if i + 1 < max_pos:
                    ways = (ways + dp[i + 1]) % MOD
                new_dp[i] = ways
            dp = new_dp
        return dp[0]

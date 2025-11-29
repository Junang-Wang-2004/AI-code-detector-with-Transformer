class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        MOD = 10**9 + 7
        dp = [[0] * (N + 1) for _ in range(L + 1)]
        dp[0][0] = 1
        for i in range(1, L + 1):
            for j in range(1, min(i, N) + 1):
                dp[i][j] = dp[i - 1][j] * max(j - K, 0) % MOD
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * j % MOD) % MOD
        return dp[L][N]

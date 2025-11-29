class Solution:
    def stringCount(self, n):
        MOD = 10**9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(2)]
        dp[0][0][0] = 1
        for _ in range(n):
            new_dp = [[[0] * 3 for _ in range(2)] for _ in range(2)]
            for hl in range(2):
                for ht in range(2):
                    for ec in range(3):
                        ways = dp[hl][ht][ec]
                        new_dp[hl][ht][ec] = (new_dp[hl][ht][ec] + ways * 23) % MOD
                        new_dp[1][ht][ec] = (new_dp[1][ht][ec] + ways) % MOD
                        new_dp[hl][1][ec] = (new_dp[hl][1][ec] + ways) % MOD
                        nec = min(ec + 1, 2)
                        new_dp[hl][ht][nec] = (new_dp[hl][ht][nec] + ways) % MOD
            dp = new_dp
        return dp[1][1][2]

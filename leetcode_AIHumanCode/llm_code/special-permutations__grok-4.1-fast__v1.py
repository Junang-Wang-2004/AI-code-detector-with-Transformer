class Solution:
    def specialPerm(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        N = 1 << n
        dp = [[0] * n for _ in range(N)]
        for i in range(n):
            dp[1 << i][i] = 1
        for mask in range(N):
            for prev in range(n):
                if dp[mask][prev] == 0:
                    continue
                for curr in range(n):
                    if mask & (1 << curr):
                        continue
                    a, b = nums[prev], nums[curr]
                    if a % b == 0 or b % a == 0:
                        dp[mask | (1 << curr)][curr] = (dp[mask | (1 << curr)][curr] + dp[mask][prev]) % MOD
        full = (1 << n) - 1
        return sum(dp[full]) % MOD if n else 1

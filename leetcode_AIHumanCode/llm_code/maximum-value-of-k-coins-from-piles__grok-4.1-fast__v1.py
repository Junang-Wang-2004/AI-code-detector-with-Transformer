class Solution:
    def maxValueOfCoins(self, piles, k):
        dp = [0] * (k + 1)
        for pile in piles:
            prefix = [0] * (len(pile) + 1)
            for idx in range(1, len(pile) + 1):
                prefix[idx] = prefix[idx - 1] + pile[idx - 1]
            for used in range(k, -1, -1):
                max_take = min(k - used, len(pile))
                for cnt in range(1, max_take + 1):
                    dp[used + cnt] = max(dp[used + cnt], dp[used] + prefix[cnt])
        return dp[k]

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                rem = n - i
                max_x = min(2 * m, rem)
                if max_x >= rem:
                    dp[i][m] = suffix[i]
                    continue
                best_opp = float('inf')
                for x in range(1, max_x + 1):
                    nxt_pos = i + x
                    nxt_m = max(m, x)
                    best_opp = min(best_opp, dp[nxt_pos][nxt_m])
                dp[i][m] = suffix[i] - best_opp
        return dp[0][1]

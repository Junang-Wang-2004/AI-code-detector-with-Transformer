class Solution:
    def mergeStones(self, piles, k):
        m = len(piles)
        if (m - 1) % (k - 1):
            return -1
        presum = [0] * (m + 1)
        for i in range(m):
            presum[i + 1] = presum[i] + piles[i]
        dp = [[0] * m for _ in range(m)]
        interval = k - 1
        for size in range(interval, m):
            for start in range(m - size):
                finish = start + size
                best = float('inf')
                p = start
                while p < finish:
                    best = min(best, dp[start][p] + dp[p + 1][finish])
                    p += interval
                dp[start][finish] = best
                if size % interval == 0:
                    dp[start][finish] += presum[finish + 1] - presum[start]
        return dp[0][m - 1]

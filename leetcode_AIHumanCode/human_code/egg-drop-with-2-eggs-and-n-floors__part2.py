# Time:  O(k * n^2)
# Space: O(n)
class Solution2(object):
    def twoEggDrop(self, n):
        """
        """
        K = 2
        dp = [[float("inf") for j in range(n+1)] for _ in range(2)]
        dp[1] = [j for j in range(n+1)]
        for i in range(2, K+1):
            dp[i%2][0] = 0
            for j in range(1, n+1):
                for k in range(1, j+1):
                    dp[i%2][j] = min(dp[i%2][j], 1+max(dp[(i-1)%2][k-1], dp[i%2][j-k]))
        return dp[K%2][n]

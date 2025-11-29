# Time:  O(k * (m * n + r))
# Space: O(m * n + r)

# dp, prefix sum
class Solution(object):
    def minCost(self, grid, k):
        """
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[float("inf")]*n for _ in range(m)]
        dp[-1][-1] = 0
        mx = max(max(row) for row in grid)
        prefix = [float("inf")]*(mx+1)
        for i in range(k+1):
            for r in reversed(range(m)):
                for c in reversed(range(n)):
                    if r+1 < m:
                        if dp[r+1][c]+grid[r+1][c] < dp[r][c]:
                            dp[r][c] = dp[r+1][c]+grid[r+1][c]
                    if c+1 < n:
                        if dp[r][c+1]+grid[r][c+1] < dp[r][c]:
                            dp[r][c] = dp[r][c+1]+grid[r][c+1]
                    if prefix[grid[r][c]] < dp[r][c]:
                        dp[r][c] = prefix[grid[r][c]]
            for r in range(m):
                for c in range(n):
                    if dp[r][c] < prefix[grid[r][c]]:
                        prefix[grid[r][c]] = dp[r][c]
            for i in range(mx):
                if prefix[i] < prefix[i+1]:
                    prefix[i+1] = prefix[i]
        return dp[0][0]



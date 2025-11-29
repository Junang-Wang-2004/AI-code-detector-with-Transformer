# Time:  O(m * n)
# Space: O(m)
# dp
class Solution2(object):
    def maxMoves(self, grid):
        """
        """
        dp = [0]*len(grid)
        for c in reversed(range(len(grid[0])-1)):
            new_dp = [0]*len(grid)
            for r in range(len(grid)):
                if grid[r][c] < grid[r][c+1]:
                    new_dp[r] = max(new_dp[r], dp[r]+1)
                if r-1 >= 0 and grid[r][c] < grid[r-1][c+1]:
                    new_dp[r] = max(new_dp[r], dp[r-1]+1)
                if r+1 < len(grid) and grid[r][c] < grid[r+1][c+1]:
                    new_dp[r] = max(new_dp[r], dp[r+1]+1)
            dp = new_dp
        return max(dp)



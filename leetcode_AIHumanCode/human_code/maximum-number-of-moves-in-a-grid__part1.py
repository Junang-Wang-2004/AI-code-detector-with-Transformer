# Time:  O(m * n)
# Space: O(m)

# dp
class Solution(object):
    def maxMoves(self, grid):
        """
        """
        dp = [True]*len(grid)
        result = 0
        for c in range(len(grid[0])-1):
            new_dp = [False]*len(grid)
            for r in range(len(grid)):
                if not dp[r]:
                    continue
                if grid[r][c] < grid[r][c+1]:
                    new_dp[r] = True
                if r-1 >= 0 and grid[r][c] < grid[r-1][c+1]:
                    new_dp[r-1] = True
                if r+1 < len(grid) and grid[r][c] < grid[r+1][c+1]:
                    new_dp[r+1] = True
            dp = new_dp
            if not sum(dp):
                break
        else:
            c = len(grid[0])-1
        return c



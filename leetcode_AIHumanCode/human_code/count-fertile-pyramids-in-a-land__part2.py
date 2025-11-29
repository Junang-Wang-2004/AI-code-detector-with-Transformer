# Time:  O(m * n)
# Space: O(m * n)
class Solution2(object):
    def countPyramids(self, grid):
        """
        """
        def count(grid):
            dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            for i in range(1, len(grid)):
                for j in range(1, len(grid[0])-1):
                    if grid[i][j] == grid[i-1][j-1] == grid[i-1][j] == grid[i-1][j+1] == 1:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+1
            return sum(sum(row) for row in dp)
        
        return count(grid) + count(grid[::-1])

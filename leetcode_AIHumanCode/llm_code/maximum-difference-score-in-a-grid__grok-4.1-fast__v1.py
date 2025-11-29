class Solution:
    def maxScore(self, grid):
        INF = 10**18 + 5
        ans = -INF
        rows = len(grid)
        cols = len(grid[0])
        for x in range(rows):
            for y in range(cols):
                leftv = grid[x][y - 1] if y > 0 else INF
                upv = grid[x - 1][y] if x > 0 else INF
                prev = min(leftv, upv)
                ans = max(ans, grid[x][y] - prev)
                grid[x][y] = min(grid[x][y], prev)
        return ans

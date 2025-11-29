class Solution(object):
    def maximumAmount(self, coins):
        m = len(coins)
        if m == 0 or len(coins[0]) == 0:
            return 0
        n = len(coins[0])
        height = max(m, n)
        width = min(m, n)
        if m <= n:
            grid = [[coins[j][i] for j in range(m)] for i in range(n)]
        else:
            grid = [row[:] for row in coins]
        prev = [float('-inf')] * width
        prev[0] = max(grid[0][0], 0)
        for j in range(1, width):
            prev[j] = prev[j - 1] + grid[0][j]
        for i in range(1, height):
            curr = [float('-inf')] * width
            curr[0] = prev[0] + grid[i][0]
            for j in range(1, width):
                curr[j] = grid[i][j] + max(prev[j], curr[j - 1])
            prev = curr
        return prev[-1]

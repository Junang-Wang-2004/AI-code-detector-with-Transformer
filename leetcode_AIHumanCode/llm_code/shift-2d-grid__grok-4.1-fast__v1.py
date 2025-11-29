class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        vals = [grid[i][j] for i in range(m) for j in range(n)]
        vals = vals[-k:] + vals[:-k]
        idx = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = vals[idx]
                idx += 1
        return grid

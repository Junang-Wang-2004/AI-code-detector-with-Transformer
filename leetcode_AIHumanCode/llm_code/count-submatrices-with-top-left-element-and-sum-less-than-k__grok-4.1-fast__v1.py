class Solution:
    def countSubmatrices(self, grid, k):
        rows = len(grid)
        cols = len(grid[0]) if grid else 0
        for r in range(rows):
            for c in range(1, cols):
                grid[r][c] += grid[r][c - 1]
        for c in range(cols):
            for r in range(1, rows):
                grid[r][c] += grid[r - 1][c]
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] <= k:
                    total += 1
        return total

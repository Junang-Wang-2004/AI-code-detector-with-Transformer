class Solution:
    def minimumOperations(self, grid):
        total = 0
        m, n = len(grid), len(grid[0])
        for j in range(n):
            prev_val = grid[0][j]
            for i in range(1, m):
                val = grid[i][j]
                if val <= prev_val:
                    required = prev_val + 1
                    total += required - val
                    prev_val = required
                else:
                    prev_val = val
        return total

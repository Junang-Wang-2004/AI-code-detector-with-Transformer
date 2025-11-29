class Solution:
    def canPartitionGrid(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        full_sum = sum(grid[r][c] for r in range(num_rows) for c in range(num_cols))
        if full_sum % 2 != 0:
            return False
        half_sum = full_sum // 2
        
        accum = 0
        for r in range(num_rows):
            row_total = sum(grid[r][c] for c in range(num_cols))
            accum += row_total
            if accum == half_sum:
                return True
            if accum > half_sum:
                break
        
        accum = 0
        for c in range(num_cols):
            col_total = sum(grid[r][c] for r in range(num_rows))
            accum += col_total
            if accum == half_sum:
                return True
            if accum > half_sum:
                break
        
        return False

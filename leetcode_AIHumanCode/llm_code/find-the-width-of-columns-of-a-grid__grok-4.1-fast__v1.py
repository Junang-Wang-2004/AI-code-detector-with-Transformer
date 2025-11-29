class Solution:
    def findColumnWidth(self, grid):
        num_rows = len(grid)
        if num_rows == 0:
            return []
        num_cols = len(grid[0])
        result = [0] * num_cols
        for col in range(num_cols):
            max_width = 0
            for row in range(num_rows):
                num_str = str(grid[row][col])
                max_width = max(max_width, len(num_str))
            result[col] = max_width
        return result

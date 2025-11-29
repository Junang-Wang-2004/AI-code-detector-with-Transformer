class Solution(object):
    def numberOfRightTriangles(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        row_counts = [sum(grid[r]) for r in range(rows)]
        col_counts = [sum(grid[r][c] for r in range(rows)) for c in range(cols)]
        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    total += (row_counts[r] - 1) * (col_counts[c] - 1)
        return total

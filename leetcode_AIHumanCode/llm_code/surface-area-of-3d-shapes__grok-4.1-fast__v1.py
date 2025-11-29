class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        tower_count = 0
        side_total = 0
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                side_total += h
                if h > 0:
                    tower_count += 1
        area += 2 * tower_count + 4 * side_total
        for i in range(n):
            for j in range(n - 1):
                area -= 2 * min(grid[i][j], grid[i][j + 1])
        for j in range(n):
            for i in range(n - 1):
                area -= 2 * min(grid[i][j], grid[i + 1][j])
        return area

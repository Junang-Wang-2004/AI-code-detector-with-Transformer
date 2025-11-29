class Solution:
    def findMaxFish(self, grid):
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def explore(r, c):
            sum_fish = grid[r][c]
            grid[r][c] = 0
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    sum_fish += explore(nr, nc)
            return sum_fish

        max_sum = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    max_sum = max(max_sum, explore(r, c))
        return max_sum

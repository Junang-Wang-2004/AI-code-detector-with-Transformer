class Solution:
    def getMaximumGold(self, grid):
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        vis = [[False] * cols for _ in range(rows)]
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def explore(r, c):
            vis[r][c] = True
            extension = 0
            for dr, dc in deltas:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0 and not vis[nr][nc]:
                    extension = max(extension, explore(nr, nc))
            vis[r][c] = False
            return grid[r][c] + extension

        maximum = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    maximum = max(maximum, explore(i, j))
        return maximum

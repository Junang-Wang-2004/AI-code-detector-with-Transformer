class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        perimeter = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] == 0:
                            perimeter += 1
        return perimeter

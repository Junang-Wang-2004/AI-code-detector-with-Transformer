class Solution:
    def countPaths(self, grid):
        MOD = 10**9 + 7
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        points = [(grid[x][y], x, y) for x in range(rows) for y in range(cols)]
        points.sort()
        ways = [[1] * cols for _ in range(rows)]
        for _, x, y in points:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[x][y] < grid[nx][ny]:
                    ways[nx][ny] = (ways[nx][ny] + ways[x][y]) % MOD
        total = 0
        for i in range(rows):
            for j in range(cols):
                total = (total + ways[i][j]) % MOD
        return total

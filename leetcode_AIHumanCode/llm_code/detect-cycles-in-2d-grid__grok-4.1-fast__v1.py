class Solution:
    def containsCycle(self, grid):
        if not grid:
            return False
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def explore(x, y, px, py):
            visited[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[x][y]:
                    if nx == px and ny == py:
                        continue
                    if visited[nx][ny]:
                        return True
                    if explore(nx, ny, x, y):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    if explore(i, j, -1, -1):
                        return True
        return False

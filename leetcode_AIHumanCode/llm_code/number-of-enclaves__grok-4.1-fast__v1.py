from collections import deque

class Solution:
    def numEnclaves(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            if grid[i][0]:
                queue.append((i, 0))
                grid[i][0] = 0
            if grid[i][n - 1]:
                queue.append((i, n - 1))
                grid[i][n - 1] = 0
        for j in range(1, n - 1):
            if grid[0][j]:
                queue.append((0, j))
                grid[0][j] = 0
            if grid[m - 1][j]:
                queue.append((m - 1, j))
                grid[m - 1][j] = 0
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in deltas:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
        return sum(sum(row) for row in grid)

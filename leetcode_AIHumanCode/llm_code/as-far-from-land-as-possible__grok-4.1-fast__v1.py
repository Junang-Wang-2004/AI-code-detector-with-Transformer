import collections

class Solution:
    def maxDistance(self, grid):
        m, n = len(grid), len(grid[0])
        total_cells = m * n
        land_positions = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land_positions.append((i, j))
        if len(land_positions) == total_cells:
            return -1
        queue = collections.deque(land_positions)
        is_visited = [[False] * n for _ in range(m)]
        for i, j in land_positions:
            is_visited[i][j] = True
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        steps = 0
        while queue:
            current_level_size = len(queue)
            for _ in range(current_level_size):
                x, y = queue.popleft()
                for dx, dy in deltas:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not is_visited[nx][ny] and grid[nx][ny] == 0:
                        is_visited[nx][ny] = True
                        queue.append((nx, ny))
            steps += 1
        return steps - 1

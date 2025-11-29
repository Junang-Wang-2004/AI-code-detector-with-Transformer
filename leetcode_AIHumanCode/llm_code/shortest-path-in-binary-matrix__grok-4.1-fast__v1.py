from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] or grid[-1][-1]:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        visited = set([(0, 0)])
        queue = deque([(0, 0, 1)])
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while queue:
            x, y, steps = queue.popleft()
            if x == rows - 1 and y == cols - 1:
                return steps
            for dx, dy in deltas:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
        return -1

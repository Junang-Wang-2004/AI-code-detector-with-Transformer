from collections import deque

class Solution:
    def hasValidPath(self, grid):
        rows, cols = len(grid), len(grid[0])
        dir_list = [
            None,
            [(0, 1), (0, -1)],
            [(-1, 0), (1, 0)],
            [(0, -1), (1, 0)],
            [(1, 0), (0, 1)],
            [(0, -1), (-1, 0)],
            [(-1, 0), (0, 1)]
        ]
        if rows == 0 or cols == 0:
            return False
        visited = set()
        q = deque([(0, 0)])
        visited.add((0, 0))
        while q:
            x, y = q.popleft()
            if x == rows - 1 and y == cols - 1:
                return True
            for dx, dy in dir_list[grid[x][y]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    ox, oy = -dx, -dy
                    if (ox, oy) in dir_list[grid[nx][ny]]:
                        q.append((nx, ny))
                        visited.add((nx, ny))
        return False

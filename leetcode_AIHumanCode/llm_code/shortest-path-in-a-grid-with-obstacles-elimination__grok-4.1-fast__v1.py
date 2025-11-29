class Solution(object):
    def shortestPath(self, grid, k):
        rows, cols = len(grid), len(grid[0])
        from collections import deque
        queue = deque()
        visited = [[[False] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        queue.append((0, 0, k, 0))
        visited[0][0][k] = True
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            cx, cy, left, length = queue.popleft()
            if cx == rows - 1 and cy == cols - 1:
                return length
            for dx, dy in deltas:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    obstacle = grid[nx][ny]
                    if obstacle == 1 and left == 0:
                        continue
                    remaining = left - obstacle
                    if not visited[nx][ny][remaining]:
                        visited[nx][ny][remaining] = True
                        queue.append((nx, ny, remaining, length + 1))
        return -1

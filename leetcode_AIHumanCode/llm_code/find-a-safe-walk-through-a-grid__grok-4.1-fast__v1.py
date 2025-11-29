from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        if not grid or not grid[0]:
            return False
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] >= health:
            return False
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        dq = deque([(0, 0)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        er, ec = rows - 1, cols - 1
        while dq:
            r, c = dq.popleft()
            if r == er and c == ec:
                return True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = 1 if grid[nr][nc] else 0
                    ndist = dist[r][c] + cost
                    if ndist < health and ndist < dist[nr][nc]:
                        dist[nr][nc] = ndist
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        return False

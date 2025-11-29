from collections import deque

class Solution:
    def maximumMinimumPath(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        vals = sorted(set(grid[i][j] for i in range(rows) for j in range(cols)))
        
        def can_reach(thresh):
            if grid[0][0] < thresh or grid[rows - 1][cols - 1] < thresh:
                return False
            vis = [[False] * cols for _ in range(rows)]
            q = deque([(0, 0)])
            vis[0][0] = True
            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while q:
                x, y = q.popleft()
                if x == rows - 1 and y == cols - 1:
                    return True
                for dx, dy in deltas:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not vis[nx][ny] and grid[nx][ny] >= thresh:
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return False
        
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if can_reach(vals[m]):
                l = m + 1
            else:
                r = m - 1
        return vals[r]

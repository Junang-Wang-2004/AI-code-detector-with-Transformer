from collections import deque

class Solution:
    def getFood(self, grid):
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        sr, sc = next((i, j) for i in range(rows) for j in range(cols) if grid[i][j] == '*')
        q = deque([(sr, sc, 0)])
        grid[sr][sc] = 'X'
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c, d = q.popleft()
            for dr, dc in deltas:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X':
                    if grid[nr][nc] == '#':
                        return d + 1
                    grid[nr][nc] = 'X'
                    q.append((nr, nc, d + 1))
        return -1

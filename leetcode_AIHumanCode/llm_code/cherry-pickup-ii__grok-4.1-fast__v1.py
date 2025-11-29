class Solution:
    def cherryPickup(self, grid):
        m, n = len(grid), len(grid[0])
        prev = [[float('-inf')] * n for _ in range(n)]
        cherries = grid[0][0] + (grid[0][n - 1] if n > 1 else 0)
        prev[0][n - 1] = cherries
        moves = [-1, 0, 1]
        for row in range(1, m):
            curr = [[float('-inf')] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if prev[x][y] == float('-inf'):
                        continue
                    for dx in moves:
                        for dy in moves:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n:
                                extra = grid[row][nx] + (grid[row][ny] if nx != ny else 0)
                                curr[nx][ny] = max(curr[nx][ny], prev[x][y] + extra)
            prev = curr
        return max(max(r) for r in prev)

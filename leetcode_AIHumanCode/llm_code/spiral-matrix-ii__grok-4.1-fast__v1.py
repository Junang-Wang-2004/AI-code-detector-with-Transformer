class Solution:
    def generateMatrix(self, n):
        grid = [[0] * n for _ in range(n)]
        x, y = 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0
        for val in range(1, n * n + 1):
            grid[x][y] = val
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0):
                d = (d + 1) % 4
                nx = x + dx[d]
                ny = y + dy[d]
            x, y = nx, ny
        return grid

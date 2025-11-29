class Solution:
    def sumRemoteness(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        total = sum(grid[i][j] for i in range(m) for j in range(n) if grid[i][j] != -1)
        visited = [[False] * n for _ in range(m)]
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def explore(x, y):
            stk = [(x, y)]
            visited[x][y] = True
            gsum = grid[x][y]
            gcount = 1
            while stk:
                cx, cy = stk.pop()
                for dx, dy in deltas:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        gsum += grid[nx][ny]
                        gcount += 1
                        stk.append((nx, ny))
            return gsum, gcount

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1 and not visited[i][j]:
                    gsum, gcount = explore(i, j)
                    ans += (total - gsum) * gcount
        return ans

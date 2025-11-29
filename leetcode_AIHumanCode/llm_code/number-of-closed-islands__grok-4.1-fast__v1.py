class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        def sink(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 0:
                return False
            grid[x][y] = 1
            sink(x - 1, y)
            sink(x + 1, y)
            sink(x, y - 1)
            sink(x, y + 1)
            return True
        for c in range(n):
            sink(0, c)
            sink(m - 1, c)
        for r in range(1, m):
            sink(r, 0)
            sink(r, n - 1)
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if sink(i, j):
                    ans += 1
        return ans

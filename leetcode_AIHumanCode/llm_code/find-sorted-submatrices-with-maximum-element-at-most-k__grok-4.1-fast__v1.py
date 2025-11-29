class Solution:
    def countSubmatrices(self, grid, k):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for col in range(n):
            w = n - col
            cur = 0
            for roww in range(m):
                if grid[roww][col] <= k:
                    cur += 1
                    ans += cur * w
                else:
                    cur = 0
        return ans

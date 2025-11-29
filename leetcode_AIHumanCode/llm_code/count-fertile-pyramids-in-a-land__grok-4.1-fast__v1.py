class Solution:
    def countPyramids(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        
        def count_direction(g):
            prev = [0] * n
            res = 0
            for i in range(1, m):
                curr = [0] * n
                for j in range(1, n - 1):
                    if (g[i][j] == 1 and g[i - 1][j - 1] == 1 and
                        g[i - 1][j] == 1 and g[i - 1][j + 1] == 1):
                        curr[j] = min(prev[j - 1], prev[j + 1]) + 1
                prev = curr
                res += sum(prev)
            return res
        
        return count_direction(grid) + count_direction(grid[::-1])

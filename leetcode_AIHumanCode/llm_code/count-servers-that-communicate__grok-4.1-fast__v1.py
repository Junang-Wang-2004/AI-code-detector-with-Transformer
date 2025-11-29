class Solution:
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])
        row_sums = [sum(r) for r in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        total = sum(row_sums)
        alone = 0
        for i in range(m):
            if row_sums[i] == 1:
                for j in range(n):
                    if grid[i][j]:
                        if col_sums[j] == 1:
                            alone += 1
                        break
        return total - alone

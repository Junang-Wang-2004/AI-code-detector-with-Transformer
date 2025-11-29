class Solution:
    def checkValidGrid(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return False
        total = m * n
        cur_r, cur_c = 0, 0
        for val in range(1, total):
            next_found = False
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == val:
                        row_diff = abs(r - cur_r)
                        col_diff = abs(c - cur_c)
                        if sorted([row_diff, col_diff]) == [1, 2]:
                            cur_r, cur_c = r, c
                            next_found = True
                        break
                if next_found:
                    break
            if not next_found:
                return False
        return True

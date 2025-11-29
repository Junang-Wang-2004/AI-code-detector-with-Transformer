class Solution:
    def lenOfVDiagonal(self, grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        se = [[1] * cols for _ in range(rows)]
        sw = [[1] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == 1:
                    ans = max(ans, 1)
                    continue
                if r > 0 and c > 0 and grid[r - 1][c - 1] == 2 - val:
                    se[r][c] = se[r - 1][c - 1] + 1
                if r > 0 and c + 1 < cols and grid[r - 1][c + 1] == 2 - val:
                    sw[r][c] = sw[r - 1][c + 1] + 1
        ne = [[1] * cols for _ in range(rows)]
        nw = [[1] * cols for _ in range(rows)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols):
                val = grid[r][c]
                if val == 1:
                    continue
                if r + 1 < rows and c > 0 and grid[r + 1][c - 1] == 2 - val:
                    ne[r][c] = ne[r + 1][c - 1] + 1
                if r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 2 - val:
                    nw[r][c] = nw[r + 1][c + 1] + 1
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == 1:
                    continue
                # SE (\) + NE (/) checking SE
                ln1 = se[r][c]
                if ln1 % 2 == val // 2:
                    pr, pc = r - ln1, c - ln1
                    if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] == 1:
                        ans = max(ans, ln1 + ne[r][c])
                # SW (/) + SE (\) checking SW
                ln2 = sw[r][c]
                if ln2 % 2 == val // 2:
                    pr, pc = r - ln2, c + ln2
                    if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] == 1:
                        ans = max(ans, ln2 + se[r][c])
                # NW (\) + SW (/) checking NW
                ln3 = nw[r][c]
                if ln3 % 2 == val // 2:
                    pr, pc = r + ln3, c + ln3
                    if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] == 1:
                        ans = max(ans, ln3 + sw[r][c])
                # NE (/) + NW (\) checking NE
                ln4 = ne[r][c]
                if ln4 % 2 == val // 2:
                    pr, pc = r + ln4, c - ln4
                    if 0 <= pr < rows and 0 <= pc < cols and grid[pr][pc] == 1:
                        ans = max(ans, ln4 + nw[r][c])
        return ans

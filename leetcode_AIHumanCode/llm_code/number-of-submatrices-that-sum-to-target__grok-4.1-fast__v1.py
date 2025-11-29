from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, grid, goal):
        if not grid or not grid[0]:
            return 0
        r = len(grid)
        c = len(grid[0])
        if r > c:
            grid = list(map(list, zip(*grid)))
            r, c = c, r
        row_cum = []
        for i in range(r):
            cum = [0] * c
            for j in range(c):
                cum[j] = (cum[j - 1] if j > 0 else 0) + grid[i][j]
            row_cum.append(cum)
        res = 0
        for top_row in range(r):
            col_cum = [0] * c
            for bot_row in range(top_row, r):
                for k in range(c):
                    col_cum[k] += row_cum[bot_row][k]
                seen = defaultdict(int)
                seen[0] = 1
                pref = 0
                for end_col in range(c):
                    pref = col_cum[end_col]
                    res += seen[pref - goal]
                    seen[pref] += 1
        return res

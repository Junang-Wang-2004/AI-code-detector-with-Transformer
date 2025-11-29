class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        rows = len(grid)
        cols = len(grid[0])
        row_prods = [1] * rows
        for r in range(rows):
            for c in range(cols):
                row_prods[r] = (row_prods[r] * grid[r][c]) % MOD
        before = [1] * (rows + 1)
        for r in range(rows):
            before[r + 1] = (before[r] * row_prods[r]) % MOD
        after = [1] * (rows + 1)
        after[rows] = 1
        for r in range(rows - 1, -1, -1):
            after[r] = (after[r + 1] * row_prods[r]) % MOD
        for r in range(rows):
            others = (before[r] * after[r + 1]) % MOD
            pref = [1] * (cols + 1)
            for c in range(cols):
                pref[c + 1] = (pref[c] * grid[r][c]) % MOD
            suff = [1] * (cols + 1)
            suff[cols] = 1
            for c in range(cols - 1, -1, -1):
                suff[c] = (suff[c + 1] * grid[r][c]) % MOD
            for c in range(cols):
                grid[r][c] = (others * pref[c] * suff[c + 1]) % MOD
        return grid

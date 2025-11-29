class Solution:
    def minFlips(self, grid):
        rows, cols = len(grid), len(grid[0])
        flips = 0
        half_r, half_c = rows // 2, cols // 2
        for i in range(half_r):
            for j in range(half_c):
                a = grid[i][j]
                b = grid[i][cols - 1 - j]
                c_ = grid[rows - 1 - i][j]
                d = grid[rows - 1 - i][cols - 1 - j]
                num_ones = a + b + c_ + d
                flips += min(num_ones, 4 - num_ones)
        mismatch = 0
        mid_ones = 0
        if rows % 2 == 1:
            mr = half_r
            for j in range(half_c):
                p = grid[mr][j]
                q = grid[mr][cols - 1 - j]
                mismatch += p ^ q
                mid_ones += p + q
        if cols % 2 == 1:
            mc = half_c
            for i in range(half_r):
                p = grid[i][mc]
                q = grid[rows - 1 - i][mc]
                mismatch += p ^ q
                mid_ones += p + q
        if rows % 2 == 1 and cols % 2 == 1:
            flips += grid[half_r][half_c]
        if mismatch == 0:
            flips += (-mid_ones) % 4
        flips += mismatch
        return flips

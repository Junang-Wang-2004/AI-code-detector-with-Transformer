class Solution:
    def countCells(self, grid, pattern):
        rows, cols = len(grid), len(grid[0])
        pat_len = len(pattern)

        def compute_z(s):
            n = len(s)
            z = [0] * n
            win_l, win_r = 0, 0
            for i in range(1, n):
                if i < win_r:
                    z[i] = min(win_r - i, z[i - win_l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] > win_r:
                    win_l, win_r = i, i + z[i]
            return z

        def get_mask(row_cnt, col_cnt, is_row_wise):
            if not is_row_wise:
                row_cnt, col_cnt = col_cnt, row_cnt
            grid_flat = ''.join(grid[x][y] for x in range(row_cnt) for y in range(col_cnt)) if is_row_wise else ''.join(grid[y][x] for x in range(row_cnt) for y in range(col_cnt))
            full = pattern + grid_flat
            z = compute_z(full)
            tot = row_cnt * col_cnt
            covered = [False] * tot
            pos = 0
            for i in range(pat_len, len(full)):
                if z[i] >= pat_len:
                    st = i - pat_len
                    pos = max(pos, st)
                    en = st + pat_len - 1
                    while pos <= en:
                        covered[pos] = True
                        pos += 1
            mask = [[False] * col_cnt for _ in range(row_cnt)]
            w = col_cnt
            for p in range(tot):
                if covered[p]:
                    mask[p // w][p % w] = True
            return mask

        hmask = get_mask(rows, cols, True)
        vmask = get_mask(rows, cols, False)
        return sum(hmask[i][j] and vmask[j][i] for i in range(rows) for j in range(cols))

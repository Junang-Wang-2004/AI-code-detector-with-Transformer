class Solution:
    def numMagicSquaresInside(self, grid):
        def check_magic(sr, sc):
            magic_sum = 15
            positions = range(3)
            row_totals = [sum(grid[sr + x][sc + y] for y in positions) for x in positions]
            if any(total != magic_sum for total in row_totals):
                return False
            col_totals = [sum(grid[sr + x][sc + y] for x in positions) for y in positions]
            if any(total != magic_sum for total in col_totals):
                return False
            main_diag = sum(grid[sr + x][sc + x] for x in positions)
            anti_diag = sum(grid[sr + x][sc + 2 - x] for x in positions)
            if main_diag != magic_sum or anti_diag != magic_sum:
                return False
            all_values = [grid[sr + x][sc + y] for x in positions for y in positions]
            return sorted(all_values) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

        m, n = len(grid), len(grid[0])
        total = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if check_magic(i, j):
                    total += 1
        return total

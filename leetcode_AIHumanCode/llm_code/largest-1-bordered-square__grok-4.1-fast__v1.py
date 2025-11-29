class Solution:
    def largest1BorderedSquare(self, grid):
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        row_sums = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                row_sums[i][j + 1] = row_sums[i][j] + grid[i][j]
        col_sums = [[0] * (n + 1) for _ in range(m)]
        for j in range(m):
            for i in range(n):
                col_sums[j][i + 1] = col_sums[j][i] + grid[i][j]
        max_side = 0
        for r in range(n):
            for c in range(m):
                possible_side = min(n - r, m - c)
                for s in range(1, possible_side + 1):
                    top_row = r
                    bot_row = r + s - 1
                    left_col = c
                    right_col = c + s - 1
                    top_full = row_sums[top_row][right_col + 1] - row_sums[top_row][left_col] == s
                    bot_full = row_sums[bot_row][right_col + 1] - row_sums[bot_row][left_col] == s
                    left_full = col_sums[left_col][bot_row + 1] - col_sums[left_col][top_row] == s
                    right_full = col_sums[right_col][bot_row + 1] - col_sums[right_col][top_row] == s
                    if top_full and bot_full and left_full and right_full:
                        max_side = max(max_side, s)
        return max_side * max_side

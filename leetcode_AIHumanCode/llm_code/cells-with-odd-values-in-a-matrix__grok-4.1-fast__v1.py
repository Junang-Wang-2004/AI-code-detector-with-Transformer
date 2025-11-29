class Solution:
    def oddCells(self, n, m, indices):
        row_toggles = {}
        col_toggles = {}
        for row_idx, col_idx in indices:
            row_toggles[row_idx] = row_toggles.get(row_idx, 0) + 1
            col_toggles[col_idx] = col_toggles.get(col_idx, 0) + 1
        odd_row_cnt = sum(val % 2 for val in row_toggles.values())
        odd_col_cnt = sum(val % 2 for val in col_toggles.values())
        return odd_row_cnt * m + odd_col_cnt * n - 2 * odd_row_cnt * odd_col_cnt

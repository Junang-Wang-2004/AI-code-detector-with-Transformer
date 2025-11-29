class Solution:
    def firstCompleteIndex(self, arr, mat):
        rows = len(mat)
        cols = len(mat[0])
        position = {}
        for r in range(rows):
            for c in range(cols):
                position[mat[r][c]] = (r, c)
        filled_rows = [0] * rows
        filled_cols = [0] * cols
        for k, num in enumerate(arr):
            row_idx, col_idx = position[num]
            filled_rows[row_idx] += 1
            filled_cols[col_idx] += 1
            if filled_rows[row_idx] == cols or filled_cols[col_idx] == rows:
                return k
        return -1

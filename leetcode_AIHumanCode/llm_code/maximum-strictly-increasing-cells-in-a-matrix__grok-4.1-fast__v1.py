class Solution(object):
    def maxIncreasingCells(self, mat):
        if not mat or not mat[0]:
            return 0
        rows = len(mat)
        cols = len(mat[0])
        cell_list = []
        for r in range(rows):
            for c in range(cols):
                cell_list.append((mat[r][c], r, c))
        cell_list.sort()
        row_max = [0] * rows
        col_max = [0] * cols
        result = 0
        idx = 0
        num_cells = len(cell_list)
        while idx < num_cells:
            current_val = cell_list[idx][0]
            current_group = []
            while idx < num_cells and cell_list[idx][0] == current_val:
                _, row_idx, col_idx = cell_list[idx]
                path_len = max(row_max[row_idx], col_max[col_idx]) + 1
                current_group.append((row_idx, col_idx, path_len))
                result = max(result, path_len)
                idx += 1
            for row_idx, col_idx, path_len in current_group:
                row_max[row_idx] = max(row_max[row_idx], path_len)
                col_max[col_idx] = max(col_max[col_idx], path_len)
        return result

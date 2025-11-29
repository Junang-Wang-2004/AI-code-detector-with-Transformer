class Solution:
    def minTotalDistance(self, grid):
        rows = []
        columns = []
        rows_count = len(grid)
        cols_count = len(grid[0]) if grid else 0
        for idx_row in range(rows_count):
            for idx_col in range(cols_count):
                if grid[idx_row][idx_col] == 1:
                    rows.append(idx_row)
                    columns.append(idx_col)
        rows.sort()
        columns.sort()
        count = len(rows)
        if count == 0:
            return 0
        center_row = rows[count // 2]
        center_col = columns[count // 2]
        result = 0
        for pos_row in rows:
            result += abs(pos_row - center_row)
        for pos_col in columns:
            result += abs(pos_col - center_col)
        return result

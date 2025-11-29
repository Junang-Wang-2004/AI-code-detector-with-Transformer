class Solution(object):
    def canPartitionGrid(self, grid):
        def possible(traversal_order, board):
            values_seen = set()
            cumsum = 0
            init_row = -1
            width = len(board[0])
            for row_idx in traversal_order:
                if init_row == -1:
                    init_row = row_idx
                for col_idx in range(width):
                    cell_val = board[row_idx][col_idx]
                    cumsum += cell_val
                    values_seen.add(cell_val)
                    adjustment = 2 * cumsum - overall_sum
                    if adjustment == 0:
                        return True
                    if row_idx != init_row and col_idx != 0:
                        if adjustment in values_seen:
                            return True
                    elif row_idx == init_row:
                        if adjustment == board[init_row][0] or adjustment == board[row_idx][col_idx]:
                            return True
                    else:
                        if adjustment == board[init_row][0] or adjustment == board[row_idx][0]:
                            return True
            return False

        overall_sum = sum(sum(r) for r in grid)
        rows = len(grid)
        cols = len(grid[0])

        fwd_rows = list(range(rows))
        if possible(fwd_rows, grid):
            return True

        rev_rows = list(range(rows - 1, -1, -1))
        if possible(rev_rows, grid):
            return True

        col_grid = [[grid[i][j] for i in range(rows)] for j in range(cols)]
        fwd_cols = list(range(cols))
        if possible(fwd_cols, col_grid):
            return True

        rev_cols = list(range(cols - 1, -1, -1))
        if possible(rev_cols, col_grid):
            return True

        return False

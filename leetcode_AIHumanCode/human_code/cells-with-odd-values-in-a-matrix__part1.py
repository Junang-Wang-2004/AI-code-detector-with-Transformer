# Time:  O(n + m)
# Space: O(n + m)

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        """
        row, col = [0]*n, [0]*m
        for r, c in indices:
            row[r] ^= 1
            col[c] ^= 1
        row_sum, col_sum = sum(row), sum(col)
        return row_sum*m+col_sum*n-2*row_sum*col_sum



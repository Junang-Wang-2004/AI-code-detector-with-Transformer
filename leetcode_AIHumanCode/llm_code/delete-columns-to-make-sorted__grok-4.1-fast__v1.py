class Solution(object):
    def minDeletionSize(self, A):
        if not A:
            return 0
        cols_to_del = 0
        width = len(A[0])
        for pos in range(width):
            prev_char = A[0][pos]
            col_ok = True
            for row in range(1, len(A)):
                curr_char = A[row][pos]
                if prev_char > curr_char:
                    col_ok = False
                    break
                prev_char = curr_char
            if not col_ok:
                cols_to_del += 1
        return cols_to_del

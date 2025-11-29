class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        num_rows, num_cols = binaryMatrix.dimensions()
        min_index = num_cols
        top_row = 0
        right_col = num_cols - 1
        while top_row < num_rows and right_col >= 0:
            if binaryMatrix.get(top_row, right_col):
                min_index = min(min_index, right_col)
                right_col -= 1
            else:
                top_row += 1
        return min_index if min_index < num_cols else -1

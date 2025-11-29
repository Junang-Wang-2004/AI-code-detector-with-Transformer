class Solution:
    def luckyNumbers(self, matrix):
        if not matrix or not matrix[0]:
            return []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        row_mins = [min(row) for row in matrix]
        col_maxes = [float('-inf')] * num_cols
        for c in range(num_cols):
            for r in range(num_rows):
                col_maxes[c] = max(col_maxes[c], matrix[r][c])
        result = []
        for r in range(num_rows):
            for c in range(num_cols):
                value = matrix[r][c]
                if value == row_mins[r] and value == col_maxes[c]:
                    result.append(value)
        return result

class Solution:
    def largestSubmatrix(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row_idx in range(rows):
            for col_idx in range(cols):
                heights[col_idx] = heights[col_idx] + 1 if matrix[row_idx][col_idx] else 0
            sorted_heights = sorted(heights)
            for pos in range(cols):
                curr_area = (cols - pos) * sorted_heights[pos]
                if curr_area > max_area:
                    max_area = curr_area
        return max_area

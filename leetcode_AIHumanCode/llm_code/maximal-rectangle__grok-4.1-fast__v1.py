class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        num_rows, num_cols = len(matrix), len(matrix[0])
        best_area = 0
        col_heights = [0] * num_cols
        for r in range(num_rows):
            for c in range(num_cols):
                if matrix[r][c] == '1':
                    col_heights[c] += 1
                else:
                    col_heights[c] = 0
            mono_stack = []
            for idx in range(num_cols + 1):
                while mono_stack and (idx == num_cols or col_heights[mono_stack[-1]] >= col_heights[idx]):
                    popped_height = col_heights[mono_stack.pop()]
                    prev_idx = mono_stack[-1] if mono_stack else -1
                    span = idx - prev_idx - 1
                    best_area = max(best_area, popped_height * span)
                if idx < num_cols:
                    mono_stack.append(idx)
        return best_area

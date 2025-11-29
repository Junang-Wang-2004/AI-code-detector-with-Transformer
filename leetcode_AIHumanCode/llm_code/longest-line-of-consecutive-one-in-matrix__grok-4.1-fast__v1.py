class Solution:
    def longestLine(self, mat):
        if not mat or not mat[0]:
            return 0
        rows, cols = len(mat), len(mat[0])
        max_length = 0
        prev_vertical = [0] * cols
        prev_diag1 = [0] * cols
        prev_diag2 = [0] * cols
        for r in range(rows):
            curr_vertical = [0] * cols
            curr_diag1 = [0] * cols
            curr_diag2 = [0] * cols
            horiz_count = 0
            for c in range(cols):
                if mat[r][c] == 0:
                    horiz_count = 0
                    curr_vertical[c] = 0
                    curr_diag1[c] = 0
                    curr_diag2[c] = 0
                    continue
                horiz_count += 1
                max_length = max(max_length, horiz_count)
                curr_vertical[c] = prev_vertical[c] + 1 if r > 0 else 1
                max_length = max(max_length, curr_vertical[c])
                curr_diag1[c] = prev_diag1[c - 1] + 1 if r > 0 and c > 0 else 1
                max_length = max(max_length, curr_diag1[c])
                curr_diag2[c] = prev_diag2[c + 1] + 1 if r > 0 and c < cols - 1 else 1
                max_length = max(max_length, curr_diag2[c])
            prev_vertical[:] = curr_vertical
            prev_diag1[:] = curr_diag1
            prev_diag2[:] = curr_diag2
        return max_length

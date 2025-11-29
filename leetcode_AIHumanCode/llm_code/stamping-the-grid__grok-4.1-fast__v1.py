class Solution:
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        rows, cols = len(grid), len(grid[0])
        zero_count = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                zero_count[i + 1][j + 1] = zero_count[i + 1][j] + zero_count[i][j + 1] - zero_count[i][j] + (1 - grid[i][j])
        can_stamp = [[0] * cols for _ in range(rows)]
        for i in range(stampHeight - 1, rows):
            for j in range(stampWidth - 1, cols):
                top = i - stampHeight + 1
                left = j - stampWidth + 1
                zeros_in_rect = (zero_count[i + 1][j + 1] - zero_count[top][j + 1] - zero_count[i + 1][left] + zero_count[top][left])
                if zeros_in_rect == stampHeight * stampWidth:
                    can_stamp[i][j] = 1
        stamp_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                stamp_prefix[i + 1][j + 1] = stamp_prefix[i + 1][j] + stamp_prefix[i][j + 1] - stamp_prefix[i][j] + can_stamp[i][j]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bot = min(i + stampHeight, rows)
                    right = min(j + stampWidth, cols)
                    covering_stamps = stamp_prefix[bot][right] - stamp_prefix[i][right] - stamp_prefix[bot][j] + stamp_prefix[i][j]
                    if covering_stamps == 0:
                        return False
        return True

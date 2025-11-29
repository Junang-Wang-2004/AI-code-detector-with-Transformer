class Solution(object):
    def differenceOfDistinctValues(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        answer = [[0] * cols for _ in range(rows)]
        def handle_diagonal(init_row, init_col):
            trackers = set()
            cur_row = init_row
            cur_col = init_col
            while cur_row < rows and cur_col < cols:
                answer[cur_row][cur_col] = len(trackers)
                trackers.add(grid[cur_row][cur_col])
                cur_row += 1
                cur_col += 1
            end_row = init_row
            end_col = init_col
            while end_row < rows and end_col < cols:
                end_row += 1
                end_col += 1
            end_row -= 1
            end_col -= 1
            trackers = set()
            cur_row = end_row
            cur_col = end_col
            while cur_row >= init_row and cur_col >= init_col:
                post_count = len(trackers)
                answer[cur_row][cur_col] = abs(answer[cur_row][cur_col] - post_count)
                trackers.add(grid[cur_row][cur_col])
                cur_row -= 1
                cur_col -= 1
        for start_col in range(cols):
            handle_diagonal(0, start_col)
        for start_row in range(1, rows):
            handle_diagonal(start_row, 0)
        return answer

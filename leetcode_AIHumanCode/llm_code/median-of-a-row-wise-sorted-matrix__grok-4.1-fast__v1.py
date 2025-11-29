class Solution(object):
    def matrixMedian(self, grid):
        num_rows = len(grid)
        if num_rows == 0:
            return 0
        num_cols = len(grid[0])
        total_elements = num_rows * num_cols

        def count_less_equal(row, target):
            start, end = 0, num_cols
            while start < end:
                pivot = (start + end) // 2
                if row[pivot] <= target:
                    start = pivot + 1
                else:
                    end = pivot
            return start

        def exceeds_half(value):
            total_count = 0
            for current_row in grid:
                total_count += count_less_equal(current_row, value)
            return total_count > total_elements // 2

        smallest = min(row[0] for row in grid)
        largest = max(row[-1] for row in grid)
        bottom, top = smallest, largest
        while bottom <= top:
            middle_value = bottom + (top - bottom) // 2
            if exceeds_half(middle_value):
                top = middle_value - 1
            else:
                bottom = middle_value + 1
        return bottom

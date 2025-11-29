class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        rows = len(grid)
        size = rows * rows
        expect_total = size * (size + 1) // 2
        expect_squares = size * (size + 1) * (2 * size + 1) // 6
        real_total = 0
        real_squares = 0
        for line in grid:
            for num in line:
                real_total += num
                real_squares += num * num
        difference = real_total - expect_total
        sq_difference = real_squares - expect_squares
        combined = sq_difference // difference
        dup = (combined + difference) // 2
        miss = (combined - difference) // 2
        return [dup, miss]

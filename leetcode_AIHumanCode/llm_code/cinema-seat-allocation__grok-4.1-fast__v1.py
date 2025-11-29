from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        row_mask = defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 5:
                row_mask[row] |= 1
            if 4 <= col <= 7:
                row_mask[row] |= 2
            if 6 <= col <= 9:
                row_mask[row] |= 4
        count = 2 * n
        for m in row_mask.values():
            if (m & 1) == 0 and (m & 4) == 0:
                continue
            if m != 7:
                count -= 1
            else:
                count -= 2
        return count

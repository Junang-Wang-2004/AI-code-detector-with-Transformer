# Time:  O(m * n)
# Space: O(1)

class Solution2(object):
    def isToeplitzMatrix(self, matrix):
        """
        """
        for row_index, row in enumerate(matrix):
            for digit_index, digit in enumerate(row):
                if not row_index or not digit_index:
                    continue
                if matrix[row_index - 1][digit_index - 1] != digit:
                    return False
        return True


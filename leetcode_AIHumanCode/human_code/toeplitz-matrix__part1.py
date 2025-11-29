# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        """
        return all(i == 0 or j == 0 or matrix[i-1][j-1] == val
                   for i, row in enumerate(matrix)
                   for j, val in enumerate(row))



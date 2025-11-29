from functools import reduce
# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def checkValid(self, matrix):
        """
        """
        return all(len(set(row)) == len(matrix) for row in matrix) and all(len(set(matrix[i][j] for i in range(len(matrix)))) == len(matrix) for j in range(len(matrix[0])))



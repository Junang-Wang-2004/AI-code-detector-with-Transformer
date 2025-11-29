class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        row = num_rows - 1
        col = 0
        
        while row >= 0 and col < num_cols:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                row -= 1
            else:
                col += 1
        
        return False

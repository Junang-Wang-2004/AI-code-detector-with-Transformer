class Solution:
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        row0_has_zero = False
        col0_has_zero = False
        
        for j in range(cols):
            if matrix[0][j] == 0:
                row0_has_zero = True
        
        for i in range(rows):
            if matrix[i][0] == 0:
                col0_has_zero = True
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if col0_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        if row0_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

class Solution:
    def matrixReshape(self, mat, target_rows, target_cols):
        if not mat or target_rows * target_cols != len(mat) * len(mat[0]):
            return mat
        
        flattened = [elem for row in mat for elem in row]
        reshaped = [flattened[i * target_cols:(i + 1) * target_cols] for i in range(target_rows)]
        return reshaped

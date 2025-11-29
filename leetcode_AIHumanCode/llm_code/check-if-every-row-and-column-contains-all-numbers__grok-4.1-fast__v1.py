class Solution:
    def checkValid(self, matrix):
        size = len(matrix)
        # Verify rows
        for row_idx in range(size):
            visited = set()
            for col_idx in range(size):
                val = matrix[row_idx][col_idx]
                if val in visited:
                    return False
                visited.add(val)
        # Verify columns
        for col_idx in range(size):
            visited = set()
            for row_idx in range(size):
                val = matrix[row_idx][col_idx]
                if val in visited:
                    return False
                visited.add(val)
        return True

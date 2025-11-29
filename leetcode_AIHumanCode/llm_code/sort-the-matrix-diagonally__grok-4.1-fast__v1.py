class Solution:
    def diagonalSort(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        for diff in range(-(cols - 1), rows):
            positions = []
            for r in range(rows):
                c = r - diff
                if 0 <= c < cols:
                    positions.append((r, c))
            values = sorted(mat[r][c] for r, c in positions)
            for i, (r, c) in enumerate(positions):
                mat[r][c] = values[i]
        return mat

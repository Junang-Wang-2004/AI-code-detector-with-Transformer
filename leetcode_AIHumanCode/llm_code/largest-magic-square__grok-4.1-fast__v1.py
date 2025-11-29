class Solution:
    def largestMagicSquare(self, grid):
        rows, cols = len(grid), len(grid[0])
        row_sums = []
        for row in grid:
            pref = [0]
            for val in row:
                pref.append(pref[-1] + val)
            row_sums.append(pref)
        col_sums = []
        for c in range(cols):
            pref = [0]
            for r in range(rows):
                pref.append(pref[-1] + grid[r][c])
            col_sums.append(pref)

        def verify_magic(sr, sc, size):
            magic_const = sum(grid[sr + k][sc + k] for k in range(size))
            if sum(grid[sr + k][sc + size - 1 - k] for k in range(size)) != magic_const:
                return False
            for i in range(sr, sr + size):
                if row_sums[i][sc + size] - row_sums[i][sc] != magic_const:
                    return False
            for j in range(sc, sc + size):
                if col_sums[j][sr + size] - col_sums[j][sr] != magic_const:
                    return False
            return True

        biggest = min(rows, cols)
        for length in range(biggest, 0, -1):
            for tr in range(rows - length + 1):
                for tc in range(cols - length + 1):
                    if verify_magic(tr, tc, length):
                        return length
        return 1

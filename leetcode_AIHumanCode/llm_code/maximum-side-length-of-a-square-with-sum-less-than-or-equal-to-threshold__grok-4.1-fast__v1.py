class Solution:
    def maxSideLength(self, mat, threshold):
        rows = len(mat)
        if rows == 0:
            return 0
        cols = len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for x in range(rows):
            for y in range(cols):
                prefix[x + 1][y + 1] = prefix[x + 1][y] + prefix[x][y + 1] - prefix[x][y] + mat[x][y]

        def has_square(k):
            for i in range(k - 1, rows):
                for j in range(k - 1, cols):
                    r1, c1 = i - k + 1, j - k + 1
                    current_sum = (prefix[i + 1][j + 1] - prefix[i + 1][c1] -
                                   prefix[r1 + 1][j + 1] + prefix[r1 + 1][c1])
                    if current_sum <= threshold:
                        return True
            return False

        low = 1
        high = min(rows, cols) + 1
        while low < high:
            middle = (low + high) // 2
            if has_square(middle):
                low = middle + 1
            else:
                high = middle
        return low - 1

class Solution:
    def matrixBlockSum(self, mat, K):
        rows, cols = len(mat), len(mat[0])
        row_cum = []
        for row in mat:
            cum = [0]
            for val in row:
                cum.append(cum[-1] + val)
            row_cum.append(cum)
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for c in range(cols + 1):
            for r in range(rows):
                prefix[r + 1][c] = prefix[r][c] + row_cum[r][c]
        ans = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                rmin, cmin = max(0, i - K), max(0, j - K)
                rmax, cmax = min(rows, i + K + 1), min(cols, j + K + 1)
                ans[i][j] = (prefix[rmax][cmax] - prefix[rmin][cmax] -
                              prefix[rmax][cmin] + prefix[rmin][cmin])
        return ans

class Solution:
    def updateMatrix(self, mat):
        if not mat or not mat[0]:
            return mat
        m, n = len(mat), len(mat[0])
        INF = 10**9
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = INF
        for i in range(m):
            for j in range(n):
                if i > 0:
                    mat[i][j] = min(mat[i][j], mat[i - 1][j] + 1)
                if j > 0:
                    mat[i][j] = min(mat[i][j], mat[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    mat[i][j] = min(mat[i][j], mat[i + 1][j] + 1)
                if j < n - 1:
                    mat[i][j] = min(mat[i][j], mat[i][j + 1] + 1)
        return mat

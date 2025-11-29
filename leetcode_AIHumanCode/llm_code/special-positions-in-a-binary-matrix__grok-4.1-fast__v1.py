class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        row_cnt = [sum(row) for row in mat]
        col_cnt = [sum(mat[r][c] for r in range(m)) for c in range(n)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and row_cnt[i] == 1 and col_cnt[j] == 1:
                    ans += 1
        return ans

class Solution(object):
    def maximumRows(self, mat, k):
        rows, n = len(mat), len(mat[0])
        rowmasks = [sum(1 << j for j in range(n) if mat[i][j]) for i in range(rows)]
        ans = 0
        for comb in range(1 << n):
            if bin(comb).count('1') == k:
                covered = sum(1 for rm in rowmasks if (rm & comb) == rm)
                ans = max(ans, covered)
        return ans

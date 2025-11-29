class Solution:
    def restoreMatrix(self, rowSum, colSum):
        m = len(rowSum)
        n = len(colSum)
        ans = [[0] * n for _ in range(m)]
        r = 0
        while r < m:
            c = 0
            while c < n and rowSum[r] > 0:
                if colSum[c] > 0:
                    val = min(rowSum[r], colSum[c])
                    ans[r][c] = val
                    rowSum[r] -= val
                    colSum[c] -= val
                c += 1
            r += 1
        return ans

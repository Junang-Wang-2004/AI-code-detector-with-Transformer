class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for clen in range(2, n + 1):
            for start in range(n - clen + 1):
                end = start + clen - 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
        return dp[0][n - 1]

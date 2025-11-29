class Solution:
    def longestPalindromicSubsequence(self, s, k):
        n = len(s)
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for rem in range(k + 1):
                dp[i][i][rem] = 1
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                for rem in range(k + 1):
                    mx = max(dp[start + 1][end][rem], dp[start][end - 1][rem])
                    delta = abs(ord(s[start]) - ord(s[end]))
                    cost = min(delta, 26 - delta)
                    if rem >= cost:
                        mx = max(mx, dp[start + 1][end - 1][rem - cost] + 2)
                    dp[start][end][rem] = mx
        return dp[0][n - 1][k]

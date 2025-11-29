class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return ""
        dp = [[False] * n for _ in range(n)]
        begin, length = 0, 1
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                begin = i
                length = 2
        for sz in range(3, n + 1):
            for i in range(n - sz + 1):
                j = i + sz - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    begin = i
                    length = sz
        return s[begin:begin + length]

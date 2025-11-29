class Solution:
    def minimumSubstringsInPartition(self, s):
        n = len(s)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for begin in range(n):
            count = [0] * 26
            unique = 0
            highest = 0
            for finish in range(begin, n):
                ch = ord(s[finish]) - ord('a')
                count[ch] += 1
                if count[ch] == 1:
                    unique += 1
                highest = max(highest, count[ch])
                win_len = finish - begin + 1
                if unique * highest == win_len:
                    dp[finish + 1] = min(dp[finish + 1], dp[begin] + 1)
        return dp[-1]

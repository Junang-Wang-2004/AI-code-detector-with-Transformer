class Solution(object):
    def minimumBeautifulSubstrings(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        pows = set()
        power = 1
        while power.bit_length() <= n:
            pows.add(power)
            power *= 5
        for begin in range(n):
            if s[begin] == '0':
                continue
            value = 0
            for finish in range(begin, n):
                value = (value << 1) | int(s[finish])
                if value in pows:
                    dp[finish + 1] = min(dp[finish + 1], dp[begin] + 1)
        ans = dp[n]
        return ans if ans != float('inf') else -1

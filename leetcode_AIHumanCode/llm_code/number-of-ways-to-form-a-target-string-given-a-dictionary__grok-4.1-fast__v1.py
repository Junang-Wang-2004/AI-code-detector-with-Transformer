class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        if not words or not target:
            return int(not target)
        cols = len(words[0])
        n = len(target)
        base = ord('a')
        freq = [[0] * 26 for _ in range(cols)]
        for c in range(cols):
            for w in words:
                idx = ord(w[c]) - base
                freq[c][idx] += 1
        dp = [[0] * (n + 1) for _ in range(cols + 1)]
        for c in range(cols + 1):
            dp[c][0] = 1
        for c in range(1, cols + 1):
            for p in range(1, n + 1):
                ch_idx = ord(target[p - 1]) - base
                dp[c][p] = (dp[c - 1][p] + dp[c - 1][p - 1] * freq[c - 1][ch_idx]) % MOD
        return dp[cols][n]

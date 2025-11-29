class Solution:
    def minimizeConcatenatedLength(self, words):
        total = sum(len(w) for w in words)
        n = len(words)
        if n == 0:
            return 0
        dp = [[float('-inf')] * 26 for _ in range(2)]
        a = ord('a')
        fs, fe = ord(words[0][0]) - a, ord(words[0][-1]) - a
        dp[0][fe] = dp[1][fs] = 0
        for k in range(1, n):
            ndp = [[float('-inf')] * 26 for _ in range(2)]
            ps, pe = ord(words[k-1][0]) - a, ord(words[k-1][-1]) - a
            cs, ce = ord(words[k][0]) - a, ord(words[k][-1]) - a
            for t in range(2):
                for x in range(26):
                    if dp[t][x] == float('-inf'):
                        continue
                    cleft = x if t else ps
                    cright = x if t == 0 else pe
                    ndp[1][cleft] = max(ndp[1][cleft], dp[t][x] + (1 if cright == cs else 0))
                    ndp[0][cright] = max(ndp[0][cright], dp[t][x] + (1 if ce == cleft else 0))
            dp = ndp
        return total - max(max(r) for r in dp)

class Solution(object):
    def numberOfArrays(self, s, k):
        MOD = 10**9 + 7
        n = len(s)
        max_digits = len(str(k))
        ways = [0] * (n + 1)
        ways[n] = 1
        for start in range(n - 1, -1, -1):
            if s[start] == '0':
                continue
            value = 0
            for pos in range(start, min(start + max_digits, n)):
                value = value * 10 + int(s[pos])
                if value > k:
                    break
                ways[start] = (ways[start] + ways[pos + 1]) % MOD
        return ways[0]

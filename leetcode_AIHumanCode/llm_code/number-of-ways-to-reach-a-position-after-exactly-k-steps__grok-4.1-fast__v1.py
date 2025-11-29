class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        MOD = 10**9 + 7
        dist = abs(endPos - startPos)
        if k < dist or (k - dist) % 2 != 0:
            return 0
        pairs = (k - dist) // 2
        ways = 1
        for i in range(1, pairs + 1):
            ways = ways * (k - i + 1) % MOD
            ways = ways * pow(i, MOD - 2, MOD) % MOD
        return ways

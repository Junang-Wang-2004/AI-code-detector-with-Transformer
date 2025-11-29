class Solution:
    def valueAfterKSeconds(self, n, k):
        MOD = 10**9 + 7
        m = n + k - 1
        r = min(k, n - 1)
        res = 1
        for i in range(r):
            res = res * (m - i) % MOD
            res = res * pow(i + 1, MOD - 2, MOD) % MOD
        return res

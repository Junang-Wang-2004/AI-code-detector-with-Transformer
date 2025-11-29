class Solution:
    def countGoodNumbers(self, n):
        mod = 10**9 + 7
        phi = mod - 1
        half = n // 2
        res = pow(20, half % phi, mod)
        if n % 2:
            res = res * 5 % mod
        return res

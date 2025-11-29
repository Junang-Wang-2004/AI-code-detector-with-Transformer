class Solution:
    def countGoodArrays(self, n, m, k):
        MOD = 10**9 + 7
        N = n - 1
        if k < 0 or k > N:
            return 0
        factorial = [1] * (N + 1)
        for i in range(1, N + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        inv_fk = pow(factorial[k], MOD - 2, MOD)
        inv_fdiff = pow(factorial[N - k], MOD - 2, MOD)
        binom = factorial[N] * inv_fk % MOD * inv_fdiff % MOD
        mult = m * pow(m - 1, N - k, MOD) % MOD
        return binom * mult % MOD

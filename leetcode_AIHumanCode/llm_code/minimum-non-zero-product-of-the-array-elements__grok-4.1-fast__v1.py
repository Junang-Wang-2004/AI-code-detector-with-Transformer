class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        PHI = MOD - 1
        power_for_exp = pow(2, p - 1, PHI)
        effective_exp = (power_for_exp - 1 + PHI) % PHI
        power_main = pow(2, p, MOD)
        big_one = (power_main - 1 + MOD) % MOD
        big_two = (power_main - 2 + MOD) % MOD
        powered_term = pow(big_two, effective_exp, MOD)
        return (big_one * powered_term) % MOD

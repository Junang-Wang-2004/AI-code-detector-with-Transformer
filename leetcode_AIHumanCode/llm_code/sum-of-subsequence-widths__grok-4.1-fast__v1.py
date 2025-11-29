class Solution:
    def sumSubseqWidths(self, A):
        MOD = 10**9 + 7
        B = sorted(A)
        n = len(B)
        
        pow2 = 1
        max_sum = 0
        for i in range(n):
            max_sum = (max_sum + B[i] * pow2) % MOD
            pow2 = (pow2 * 2) % MOD
        
        pow2 = 1
        min_sum = 0
        for i in range(n - 1, -1, -1):
            min_sum = (min_sum + B[i] * pow2) % MOD
            pow2 = (pow2 * 2) % MOD
        
        return (max_sum - min_sum + MOD) % MOD

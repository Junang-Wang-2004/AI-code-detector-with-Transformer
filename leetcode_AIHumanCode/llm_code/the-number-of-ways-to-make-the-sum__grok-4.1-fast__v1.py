class Solution:
    def numberOfWays(self, n):
        MOD = 10**9 + 7
        
        def count_ways(rem):
            if rem < 0:
                return 0
            q = rem // 6
            p = rem // 2
            term1 = (p + 1) * (q + 1)
            term2 = 3 * q * (q + 1) // 2
            return (term1 - term2) % MOD
        
        result = 0
        for num_fours in range(3):
            leftover = n - num_fours * 4
            result = (result + count_ways(leftover)) % MOD
        return result

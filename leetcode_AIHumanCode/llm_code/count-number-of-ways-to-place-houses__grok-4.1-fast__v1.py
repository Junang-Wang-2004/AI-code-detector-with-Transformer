class Solution:
    def countHousePlacements(self, n):
        MOD = 10**9 + 7
        prev0 = 1
        prev1 = 2
        for i in range(2, n + 1):
            next_val = (prev0 + prev1) % MOD
            prev0 = prev1
            prev1 = next_val
        return pow(prev1, 2, MOD)

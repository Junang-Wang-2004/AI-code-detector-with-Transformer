class Solution:
    def subsequenceCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        if n == 0:
            return 0
        has_odd = any(num & 1 for num in nums)
        if not has_odd:
            return 0
        result = 1
        for _ in range(n - 1):
            result = result * 2 % MOD
        return result

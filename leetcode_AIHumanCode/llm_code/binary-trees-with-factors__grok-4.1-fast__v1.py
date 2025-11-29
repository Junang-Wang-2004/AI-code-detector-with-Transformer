class Solution:
    def numFactoredBinaryTrees(self, A):
        MOD = 10**9 + 7
        nums = sorted(A)
        n = len(nums)
        if n == 0:
            return 0
        val_idx = {nums[k]: k for k in range(n)}
        ways = [1] * n
        result = 0
        for p in range(n):
            for q in range(p):
                if nums[p] % nums[q] != 0:
                    continue
                factor = nums[p] // nums[q]
                if factor in val_idx:
                    ways[p] = (ways[p] + ways[q] * ways[val_idx[factor]]) % MOD
            result = (result + ways[p]) % MOD
        return result

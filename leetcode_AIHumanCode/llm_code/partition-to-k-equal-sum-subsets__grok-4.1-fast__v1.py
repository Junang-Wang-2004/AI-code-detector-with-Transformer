class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if max(nums) > target:
            return False
        n = len(nums)
        full = (1 << n) - 1
        mod_sums = [0] * (1 << n)
        for i in range(n):
            bit = 1 << i
            num_mod = nums[i] % target
            for mask in range(1 << n):
                if (mask & bit) == 0:
                    mod_sums[mask | bit] = (mod_sums[mask] + num_mod) % target
        dp = [False] * (1 << n)
        dp[0] = True
        for mask in range(1 << n):
            if not dp[mask]:
                continue
            partial = mod_sums[mask]
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    continue
                if partial + nums[i] > target:
                    continue
                new_mask = mask | (1 << i)
                dp[new_mask] = True
        return dp[full]

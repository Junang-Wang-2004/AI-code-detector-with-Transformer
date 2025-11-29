class Solution:
    def minSubarray(self, nums, p):
        total_mod = sum(nums) % p
        if total_mod == 0:
            return 0
        n = len(nums)
        ans = n
        mod_to_idx = {0: -1}
        prefix_mod = 0
        for i in range(n):
            prefix_mod = (prefix_mod + nums[i]) % p
            prev_mod = (prefix_mod - total_mod + p) % p
            if prev_mod in mod_to_idx:
                ans = min(ans, i - mod_to_idx[prev_mod])
            mod_to_idx[prefix_mod] = i
        return ans if ans < n else -1

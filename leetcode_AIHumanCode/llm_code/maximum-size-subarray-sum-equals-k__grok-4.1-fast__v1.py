class Solution:
    def maxSubArrayLen(self, nums, k):
        prefix_map = {0: -1}
        prefix_sum = 0
        ans = 0
        for idx, val in enumerate(nums):
            prefix_sum += val
            target_prefix = prefix_sum - k
            if target_prefix in prefix_map:
                ans = max(ans, idx - prefix_map[target_prefix])
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = idx
        return ans

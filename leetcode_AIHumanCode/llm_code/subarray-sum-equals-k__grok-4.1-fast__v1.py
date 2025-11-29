class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        prefix_sum = 0
        freq_map = {0: 1}
        for value in nums:
            prefix_sum += value
            ans += freq_map.get(prefix_sum - k, 0)
            freq_map[prefix_sum] = freq_map.get(prefix_sum, 0) + 1
        return ans

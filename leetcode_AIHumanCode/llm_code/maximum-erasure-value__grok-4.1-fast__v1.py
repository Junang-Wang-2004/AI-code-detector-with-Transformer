class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        cur_sum = 0
        max_sum = 0
        start = 0
        for end in range(len(nums)):
            while nums[end] in seen:
                cur_sum -= nums[start]
                seen.remove(nums[start])
                start += 1
            seen.add(nums[end])
            cur_sum += nums[end]
            max_sum = max(max_sum, cur_sum)
        return max_sum

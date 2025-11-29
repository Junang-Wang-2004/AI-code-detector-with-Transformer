class Solution:
    def maxIncreasingSubarrays(self, nums):
        ans = 0
        length = 1
        prior = 0
        n = len(nums)
        i = 1
        while i < n:
            if nums[i - 1] < nums[i]:
                length += 1
            else:
                ans = max(ans, length // 2, min(prior, length))
                prior = length
                length = 1
            i += 1
        ans = max(ans, length // 2, min(prior, length))
        return ans

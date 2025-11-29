# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        """
        result = cnt = 1 if len(nums) == 1 or cmp(nums[0], nums[1]) == 0 else 2
        for i in range(2, len(nums)):
            cnt = 1 if cmp(nums[i-1], nums[i]) == 0 else cnt+1 if cmp(nums[i-2], nums[i-1]) == cmp(nums[i-1], nums[i]) else 2
            result = max(result, cnt)
        return result



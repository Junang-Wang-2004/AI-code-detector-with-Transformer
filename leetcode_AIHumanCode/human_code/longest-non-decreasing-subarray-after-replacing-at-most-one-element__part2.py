# Time:  O(n)
# Space: O(n)
# prefix sum
class Solution2(object):
    def longestSubarray(self, nums):
        """
        """
        left = [1]*len(nums)
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                left[i+1] = left[i]+1
        right = [1]*len(nums)
        for i in reversed(range(len(nums)-1)):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1]+1
        result = min(max(left)+1, len(nums))
        for i in range(1, len(nums)-1):
            if nums[i-1] <= nums[i+1]:
                result = max(result, left[i-1]+1+right[i+1])
        return result

# Time:  O(n)
# Space: O(1)

# prefix sum, math
class Solution(object):
    def maximumSumScore(self, nums):
        """
        """
        prefix = suffix = 0
        result = float("-inf")
        right = len(nums)-1
        for left in range(len(nums)):
            prefix += nums[left]
            suffix += nums[right]
            right -= 1
            result = max(result, prefix, suffix)
        return result

    

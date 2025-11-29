# Time:  O(n)
# Space: O(n)

# prefix sum
class Solution(object):
    def longestSubarray(self, nums):
        """
        """
        right = [1]*len(nums)
        for i in reversed(range(len(nums)-1)):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1]+1
        result = min(max(right)+1, len(nums))
        left = 1
        for i in range(1, len(nums)-1):
            if nums[i-1] <= nums[i+1]:
                result = max(result, left+1+right[i+1])
            if nums[i-1] <= nums[i]:
                left += 1
            else:
                left = 1
        return result



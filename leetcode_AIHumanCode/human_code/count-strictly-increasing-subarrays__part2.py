# Time:  O(n)
# Space: O(1)
# two pointers
class Solution2(object):
    def countSubarrays(self, nums):
        """
        """
        result = left = 0
        for right in range(len(nums)):
            if not (right-1 >= 0 and nums[right-1] < nums[right]):
                left = right
            result += right-left+1
        return result

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestSubarray(self, nums):
        """
        """
        count, left = 0, 0
        for right in range(len(nums)):
            count += (nums[right] == 0)
            if count >= 2:
                count -= (nums[left] == 0)
                left += 1
        return (right-left+1)-1



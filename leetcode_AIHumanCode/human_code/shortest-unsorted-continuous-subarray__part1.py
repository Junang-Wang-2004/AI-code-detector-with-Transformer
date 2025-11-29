# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        """
        n = len(nums)
        left, right = -1, -2
        min_from_right, max_from_left = nums[-1], nums[0]
        for i in range(1, n):
            max_from_left = max(max_from_left, nums[i])
            min_from_right = min(min_from_right, nums[n-1-i])
            if nums[i] < max_from_left: right = i
            if nums[n-1-i] > min_from_right: left = n-1-i



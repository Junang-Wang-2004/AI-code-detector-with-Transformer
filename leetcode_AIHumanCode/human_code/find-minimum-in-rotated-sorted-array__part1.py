# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        """
        left, right = 0, len(nums)
        target = nums[-1]

        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1

        return nums[left]



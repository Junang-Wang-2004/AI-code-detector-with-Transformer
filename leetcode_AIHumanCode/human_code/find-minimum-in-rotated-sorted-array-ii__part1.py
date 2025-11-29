# Time:  O(logn) ~ O(n)
# Space: O(1)

class Solution(object):
    def findMin(self, nums):
        """
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]



# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def triangleNumber(self, nums):
        """
        """
        result = 0
        nums.sort()
        for i in reversed(range(2, len(nums))):
            left, right = 0, i-1
            while left < right:
                if nums[left]+nums[right] > nums[i]:
                    result += right-left
                    right -= 1
                else:
                    left += 1
        return result



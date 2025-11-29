# Time:  O(n^3)
# Space: O(1)
# brute force
class Solution2(object):
    def incremovableSubarrayCount(self, nums):
        """
        """
        return sum((left == 0 or right == len(nums)-1 or nums[left-1] < nums[right+1]) and
                   all(nums[i] < nums[i+1] for i in range(left-1)) and
                   all(nums[i] < nums[i+1] for i in range(right+1, len(nums)-1))
                   for left in range(len(nums)) for right in range(left, len(nums)))

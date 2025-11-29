# Time:  O(nlogn)
# Space: O(n)
# sort
class Solution3(object):
    def sortEvenOdd(self, nums):
        """
        """
        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        return nums
